# walmart_stormy_workflow.py
import os
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import GroupKFold, train_test_split
from sklearn.metrics import mean_squared_log_error
from sklearn.ensemble import RandomForestRegressor
try:
    from lightgbm import LGBMRegressor
    has_lgb = True
except Exception:
    has_lgb = False

RANDOM_STATE = 42

# ------------------------
# Utilities / Metrics
# ------------------------
def rmsle(y_true, y_pred):
    # compute RMSLE robustly (digit-by-digit attention)
    # ensure no negative predictions
    y_pred = np.maximum(0, y_pred)
    return np.sqrt(mean_squared_log_error(y_true, y_pred))

# ------------------------
# Load / Basic cleaning
# ------------------------
def load_data(train_path, stores_path=None, items_path=None, weather_path=None, parse_dates=['date']):
    """
    Load CSVs. Return a dictionary of DataFrames.
    """
    out = {}
    out['train'] = pd.read_csv(train_path, parse_dates=parse_dates)
    if stores_path:
        out['stores'] = pd.read_csv(stores_path)
    if items_path:
        out['items'] = pd.read_csv(items_path)
    if weather_path:
        out['weather'] = pd.read_csv(weather_path, parse_dates=parse_dates)
    return out

def basic_cleaning(df):
    """
    Minimal cleaning for common issues:
      - drop duplicates
      - fill or mark missing numeric weather values with sentinel or interpolation
    """
    df = df.copy()
    df = df.drop_duplicates()
    # Example: if there's a 'units' or 'sales' target column, ensure non-negative
    for col in df.select_dtypes(include=[np.number]).columns:
        # small rule: replace infinite with nan -> later fill
        df[col].replace([np.inf, -np.inf], np.nan, inplace=True)
    return df

# ------------------------
# Baseline estimation
# ------------------------
def compute_baseline(df, group_cols=['store_nbr','item_nbr'], date_col='date', target_col='units'):
    """
    A simple baseline: median sales per (group, day_of_week) or per group.
    Returns baseline series aligned with df index named 'baseline'.
    """
    tmp = df.copy()
    tmp['dayofweek'] = tmp[date_col].dt.dayofweek
    # baseline per group + dayofweek where possible
    base = tmp.groupby(group_cols + ['dayofweek'])[target_col].median().reset_index()
    base = base.rename(columns={target_col: 'baseline'})
    merged = tmp.merge(base, on=group_cols + ['dayofweek'], how='left')
    # if baseline missing (new combos), fallback to group median
    group_med = tmp.groupby(group_cols)[target_col].median().reset_index().rename(columns={target_col: 'group_median'})
    merged = merged.merge(group_med, on=group_cols, how='left')
    merged['baseline'] = merged['baseline'].fillna(merged['group_median']).fillna(0)
    return merged['baseline'].values

# ------------------------
# Feature engineering
# ------------------------
def add_time_features(df, date_col='date'):
    df = df.copy()
    df['day'] = df[date_col].dt.day
    df['month'] = df[date_col].dt.month
    df['year'] = df[date_col].dt.year
    df['dayofweek'] = df[date_col].dt.dayofweek
    df['weekofyear'] = df[date_col].dt.isocalendar().week.astype(int)
    df['is_weekend'] = df['dayofweek'].isin([5,6]).astype(int)
    # day of month fractional (cyclic)
    df['day_sin'] = np.sin(2 * np.pi * df['day'] / 31)
    df['day_cos'] = np.cos(2 * np.pi * df['day'] / 31)
    return df

def add_weather_features(df, weather_df, merge_on=['store_nbr','date']):
    """
    Merge weather; weather_df assumed to have date and weather station mapping.
    Replace missing numeric weather with 0 or forward/backfill as appropriate.
    """
    df = df.copy()
    if weather_df is None:
        return df
    # Basic merge
    merged = df.merge(weather_df, on=merge_on, how='left', suffixes=('','_w'))
    # example fills - adapt as needed
    numeric_cols = merged.select_dtypes(include=[np.number]).columns.tolist()
    # don't fill target or identifiers
    numeric_cols = [c for c in numeric_cols if c not in ['units','baseline','store_nbr','item_nbr']]
    merged[numeric_cols] = merged[numeric_cols].fillna(0)
    return merged

def add_lag_roll_features(df, group_cols=['store_nbr','item_nbr'], date_col='date', target_col='units',
                          lags=[1,7,14], windows=[3,7,14]):
    """
    Add lag features and rolling mean/std. Dataframe must be sorted by date within group.
    """
    df = df.copy()
    df = df.sort_values(group_cols + [date_col])
    for lag in lags:
        df[f'lag_{lag}'] = df.groupby(group_cols)[target_col].shift(lag)
    for w in windows:
        df[f'roll_mean_{w}'] = df.groupby(group_cols)[target_col].shift(1).rolling(window=w, min_periods=1).mean().reset_index(level=group_cols, drop=True)
        df[f'roll_std_{w}'] = df.groupby(group_cols)[target_col].shift(1).rolling(window=w, min_periods=1).std().reset_index(level=group_cols, drop=True).fillna(0)
    # Fill lag NAs with 0 (or better: global median)
    lag_cols = [c for c in df.columns if c.startswith('lag_') or c.startswith('roll_')]
    df[lag_cols] = df[lag_cols].fillna(0)
    return df

def add_holiday_and_storm_flags(df, holidays=None, storm_windows=None, date_col='date'):
    """
    holidays: list of dates or DataFrame with date column
    storm_windows: list of tuples (start_date, end_date) or DataFrame with start/end
    Adds:
      - is_holiday
      - days_to_nearest_holiday (signed)
      - is_in_storm_window
    """
    df = df.copy()
    if holidays is None:
        holidays = []
    if isinstance(holidays, (list, tuple)):
        hol_dates = pd.to_datetime(holidays)
    else:
        hol_dates = pd.to_datetime(holidays[date_col]) if 'date' in holidays.columns else pd.to_datetime([])

    df['is_holiday'] = df[date_col].isin(hol_dates).astype(int)
    # days to nearest holiday (simple approach)
    if len(hol_dates) > 0:
        hol_array = np.sort(hol_dates.values)
        # for each date compute min difference
        df['days_to_holiday'] = df[date_col].apply(lambda x: int(np.min(np.abs((hol_array - np.datetime64(x)).astype('timedelta64[D]')).astype(int))) if len(hol_array)>0 else 999)
    else:
        df['days_to_holiday'] = 999

    # storm windows
    df['is_in_storm'] = 0
    if storm_windows:
        # storm_windows: list of (start, end)
        for s, e in storm_windows:
            s = pd.to_datetime(s); e = pd.to_datetime(e)
            mask = (df[date_col] >= s) & (df[date_col] <= e)
            df.loc[mask, 'is_in_storm'] = 1
    return df

# ------------------------
# Prepare dataset for modeling
# ------------------------
def prepare_model_data(df, date_col='date', target_col='units', group_cols=['store_nbr','item_nbr'], drop_cols=None):
    """
    Returns (X, y, meta_df)
    - baseline is computed and subtracted from target; model will predict residual
    """
    df = df.copy()
    if drop_cols is None:
        drop_cols = []
    # baseline
    df['baseline'] = compute_baseline(df, group_cols=group_cols, date_col=date_col, target_col=target_col)
    # residual: target - baseline (but we will model log1p y and log1p baseline)
    # We'll model residual in real domain after log1p -> simpler to predict log-delta? Simpler: model target_log - baseline_log
    df['y_raw'] = df[target_col].values
    # transform
    df['y'] = np.log1p(df['y_raw'])
    df['baseline_log'] = np.log1p(df['baseline'])
    df['y_minus_baseline'] = df['y'] - df['baseline_log']  # model this quantity (can be negative)
    # Features: numeric and categorical
    # Drop identifiers and raw target
    reserved = set([target_col, 'y_raw', 'y', 'baseline', 'baseline_log'])
    reserved.update(drop_cols)
    feature_cols = [c for c in df.columns if c not in reserved and c not in group_cols and c != date_col]
    X = df[feature_cols].copy()
    y = df['y_minus_baseline'].copy()
    return X, y, df

# ------------------------
# Modeling
# ------------------------
def fit_model(X_train, y_train, X_valid=None, y_valid=None, model_type='lgb', params=None):
    if params is None:
        params = {}
    if model_type == 'lgb' and has_lgb:
        model = LGBMRegressor(random_state=RANDOM_STATE, n_estimators=1000, **params)
        fit_args = {}
        if X_valid is not None:
            fit_args['eval_set'] = [(X_valid, y_valid)]
            fit_args['early_stopping_rounds'] = 50
        model.fit(X_train, y_train, **fit_args)
    else:
        # fallback to RandomForest
        model = RandomForestRegressor(n_estimators=200, random_state=RANDOM_STATE, n_jobs=-1)
        model.fit(X_train, y_train)
    return model

def predict_and_assemble(model, X, df_meta):
    """
    Given model predicting y_minus_baseline = log1p(y_raw) - log1p(baseline)
    Reconstruct predicted raw units:
      pred_log = pred + baseline_log
      pred_raw = expm1(pred_log)
    """
    pred_delta = model.predict(X)
    pred_log = pred_delta + df_meta['baseline_log'].values
    pred_raw = np.expm1(pred_log)
    # ensure non-negative
    pred_raw = np.maximum(0, pred_raw)
    return pred_raw

# ------------------------
# Example pipeline / usage
# ------------------------
def example_pipeline(train_csv, weather_csv=None, stores_csv=None, items_csv=None,
                     date_col='date', target_col='units'):
    # load
    data = load_data(train_csv, stores_path=stores_csv, items_path=items_csv, weather_path=weather_csv)
    df = data['train']
    df = basic_cleaning(df)
    if 'date' not in df.columns:
        raise ValueError("Expect a 'date' column")
    # Add time features
    df = add_time_features(df, date_col=date_col)
    # Merge weather if provided
    if 'weather' in data:
        df = add_weather_features(df, data['weather'], merge_on=['store_nbr','date'])
    # Add holiday/storm placeholders (you should supply actual dates/windows)
    # Example: a couple of holiday dates
    holidays = ['2016-12-25','2017-01-01']
    # Example: storm windows: list of tuples (start, end)
    storm_windows = [('2017-01-20','2017-01-24')]
    df = add_holiday_and_storm_flags(df, holidays=holidays, storm_windows=storm_windows, date_col=date_col)
    # Add lag/rolling features
    df = add_lag_roll_features(df, group_cols=['store_nbr','item_nbr'], date_col=date_col, target_col=target_col)
    # Prepare model data
    X, y, meta = prepare_model_data(df, date_col=date_col, target_col=target_col)
    # Simple train/valid split: group by storm windows or by time. We'll do a time split to mimic forecasting.
    # Use latest 20% dates as validation
    sorted_dates = np.sort(df[date_col].unique())
    cutoff_date = sorted_dates[int(len(sorted_dates)*0.8)]
    is_valid = df[date_col] > cutoff_date
    X_train, X_valid = X.loc[~is_valid], X.loc[is_valid]
    y_train, y_valid = y.loc[~is_valid], y.loc[is_valid]
    meta_train, meta_valid = meta.loc[~is_valid], meta.loc[is_valid]
    # Fit model
    model = fit_model(X_train, y_train, X_valid, y_valid, model_type='lgb')
    # Predict and assemble back to raw units
    pred_valid = predict_and_assemble(model, X_valid, meta_valid)
    # Evaluate RMSLE on validation
    score = rmsle(meta_valid[target_col].values, pred_valid)
    print("Validation RMSLE:", score)
    # Feature importance (if available)
    try:
        importances = model.feature_importances_
        fi = pd.Series(importances, index=X.columns).sort_values(ascending=False).head(30)
        print("Top features:\n", fi)
    except Exception:
        pass
    return model, X_train, y_train, X_valid, y_valid, meta_valid

# If running as script
if __name__ == "__main__":
    # Example usage (change paths)
    # model, X_train, y_train, X_valid, y_valid, meta_valid = example_pipeline('train.csv', weather_csv='weather.csv')
    pass
