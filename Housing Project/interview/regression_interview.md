# 📈 Regression Modeling Interview Questions

## ✅ What is linear regression?

**Linear Regression** is a statistical method used to model the relationship between a **dependent variable (target)** and one or more **independent variables (features)** by fitting a linear equation to the observed data.  
- In simple linear regression, the relationship is modeled as:  
  `y = β₀ + β₁x + ε`,  
  where:
  - `y` is the dependent variable
  - `x` is the independent variable
  - `β₀` is the intercept
  - `β₁` is the coefficient (slope)
  - `ε` is the error term (residual)

---

## 📋 What are the assumptions of OLS linear regression?

OLS (Ordinary Least Squares) linear regression relies on several key assumptions:

1. **Linearity**: The relationship between the predictors and the response is linear.
2. **Independence**: Observations are independent of each other.
3. **Homoscedasticity**: Constant variance of the errors (no heteroscedasticity).
4. **Normality of errors**: The residuals are normally distributed.
5. **No multicollinearity**: Predictors are not highly correlated with each other.
6. **No autocorrelation**: Particularly important in time series data — residuals should not be correlated.

---

## ⚠️ What happens when OLS assumptions are violated?

Violating these assumptions can lead to unreliable or misleading estimates:

- **Linearity violated**: The model won't capture the true relationship → underfitting.
- **Heteroscedasticity**: Standard errors may be incorrect → unreliable confidence intervals and p-values.
- **Multicollinearity**: Coefficients become unstable and hard to interpret.
- **Autocorrelation**: Leads to underestimated standard errors and inflated t-statistics.
- **Non-normal residuals**: Affects hypothesis testing; estimates may still be unbiased but inference suffers.

---

## 📊 How do you evaluate a regression model?

Several metrics and plots are commonly used:

1. **R² (R-squared)**: Proportion of variance explained by the model.
2. **Adjusted R²**: Adjusted for number of predictors; penalizes model complexity.
3. **Mean Absolute Error (MAE)**: Average absolute errors.
4. **Mean Squared Error (MSE)** and **Root Mean Squared Error (RMSE)**.
5. **Residual plots**: To check for patterns and assumptions.
6. **QQ plots**: To evaluate normality of residuals.
7. **F-statistic**: Overall significance of the regression.

---

## 🔍 What is the difference between R² and adjusted R²?

| Metric         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **R²**         | Measures proportion of variance explained by the model. Always increases as more variables are added. |
| **Adjusted R²**| Penalizes for adding variables that do not improve the model. Helps prevent overfitting. |

> **Key difference**: Adjusted R² accounts for the number of predictors, whereas R² does not.

---

## 📚 What are some different types of regression models?

1. **Simple Linear Regression** – One independent variable.
2. **Multiple Linear Regression** – Multiple independent variables.
3. **Polynomial Regression** – Fits a nonlinear relationship using higher-degree terms.
4. **Ridge Regression** – L2 regularization to prevent overfitting.
5. **Lasso Regression** – L1 regularization for feature selection.
6. **Elastic Net** – Combination of L1 and L2 regularization.
7. **Logistic Regression** – For binary outcomes (classification).
8. **Quantile Regression** – Estimates conditional quantiles (like median).
9. **Robust Regression** – Deals with outliers better than OLS.

---
