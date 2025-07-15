# Housing Price Analysis with Python

This project analyzes housing price data using Python libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn`. The focus is on exploring the `SalePrice` variable, transforming it, and visualizing its relationship with other variables to support data-driven decision-making.

## Project Structure

```bash
housing_price_analysis/
├── housing_data.csv         # Raw dataset
├── analysis.py              # Python script for analysis
├── README.md                # Project documentation (this file)
```

## Tools & Libraries

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

## Objectives

- Explore and summarize the distribution of housing sale prices.
- Apply log transformation to normalize skewed data.
- Visualize relationships between `SalePrice` and key numeric variables.

## Data Loading

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

housing_data = pd.read_csv('housing_data.csv')
```

## Descriptive Statistics

```python
# Basic info and SalePrice summary
housing_data.columns
housing_data['SalePrice'].describe()
```

## Histogram of Sale Prices

```python
sns.displot(housing_data['SalePrice'])
plt.show()
```

## Log Transformation of Sale Price

```python
log_data = np.log(housing_data['SalePrice'])
print(log_data.skew())
sns.displot(log_data)
plt.show()
```

## Scatter Plots

### 1st Floor Square Footage vs Sale Price
```python
data = pd.concat([housing_data['SalePrice'], housing_data['1stFlrSF']], axis=1)
data.plot.scatter(x='1stFlrSF', y='SalePrice', ylim=(0,800000))
plt.show()
```

### Garage Area vs Sale Price
```python
data = pd.concat([housing_data['SalePrice'], housing_data['GarageArea']], axis=1)
data.plot.scatter(x='GarageArea', y='SalePrice', ylim=(0,800000))
plt.show()
```

## Boxplot of Sale Price by Year Built

```python
data = pd.concat([housing_data['SalePrice'], housing_data['YearBuilt']], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x='YearBuilt', y='SalePrice', data=data)
fig.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
plt.show()
```

## Key Insights

- Sale prices are right-skewed and benefit from log transformation.
- Strong positive correlation exists between SalePrice and variables like `1stFlrSF`, `GarageArea`.
- SalePrice tends to increase with more recent construction years.

## How to Run

1. Clone the repository
2. Place your `housing_data.csv` file in the project folder
3. Run `housing.py` or execute the code cells in a Jupyter Notebook or Python environment

```bash
python housing.py
```

---

