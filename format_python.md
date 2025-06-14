```Python
rate_of_return= 0.075

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

print(display_as_percentage(rate_of_return))


def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_simple_return(start_price, end_price, dividend=0):
  return (end_price - start_price + dividend) / start_price

simple_return = calculate_simple_return(200, 250, 20)

print('The simple rate of return is', display_as_percentage(simple_return))


# Import library here
from math import log

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_log_return(start_price, end_price):
  return log(end_price / start_price)

log_return = calculate_log_return(200, 250)

print('The log rate of return is', display_as_percentage(log_return))


def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

daily_return_a = 0.001
monthly_return_b = 0.022

# Write code here
print('The daily rate of return for Investment A is', display_as_percentage(daily_return_a))

print('The monthly rate of return for Investment B is', display_as_percentage(monthly_return_b))

def annualize_return(log_return, t):
  return log_return * t

annual_return_a = annualize_return(daily_return_a, 252)
print('The annual rate of return for Investment A is', display_as_percentage(annual_return_a))

annual_return_b = annualize_return(monthly_return_b, 12)
print('The annual rate of return for Investment B is', display_as_percentage(annual_return_b))


def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]

# Write code here
def convert_returns(log_returns, t):
  return sum(log_returns) / len(log_returns) * t

annual_return = convert_returns(daily_returns, 252)

print('The annual rate of return is', display_as_percentage(annual_return))

weekly_return = convert_returns(daily_returns, 5)
weekly_return = sum(daily_returns)

print('The weekly rate of return is', display_as_percentage(weekly_return))


import numpy as np

returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]

variance_disney = np.var(returns_disney)
variance_cbs = np.var(returns_cbs)

# Write code here
dataset = [10, 8, 9, 10, 12]

def calculate_variance(dataset):
  mean = sum(dataset) / len(dataset)

  numerator = 0
  for data in dataset:
    numerator += (data - mean) ** 2

  variance = numerator / len(dataset)
  
  return variance

variance_disney = calculate_variance(returns_disney)
variance_cbs = calculate_variance(returns_cbs)

print('The variance of Disney stock returns is', variance_disney)
print('The variance of CBS stock returns is', variance_cbs)


from utils import calculate_variance
import numpy as np
# Import library here
from math import sqrt

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]

stddev_disney = np.std(returns_disney)
stddev_cbs = np.std(returns_cbs)

# Write code here
dataset = [10, 8, 9, 10, 12]

def calculate_stddev(dataset):
  variance = calculate_variance(dataset)

  stddev = sqrt(variance)

  return stddev

stddev_disney = calculate_stddev(returns_disney)
stddev_cbs = calculate_stddev(returns_cbs)

print('The standard deviation of Disney stock returns is', display_as_percentage(stddev_disney))
print('The standard deviation of CBS stock returns is', display_as_percentage(stddev_cbs))
```

Correlation is a measure of how closely two datasets are associated with each other. It is often represented by the correlation coefficient, which is a value that ranges between -1 and 1. This indicates whether there is a positive correlation, negative correlation, or no correlation:

Positive correlation – when the rate of 
Preview: Docs Loading link description
return
 of one asset deviates upward from its mean, the other usually deviates upward as well.

Negative correlation – when the rate of return of one asset deviates upward from its mean, the other usually deviates downward.

No correlation – when a change in one asset’s rate of return does not dictate a change in another. The correlation coefficient will be close to 0.

```Python 
from utils import calculate_correlation
import numpy as np

returns_general_motors = [0.018, -0.005, -0.047, -0.009, -0.012, 0.003, -0.027, -0.014, 0.029, -0.062, 0.009]
returns_ford = [0.002, -0.004, -0.027, -0.022, -0.001, 0.002, -0.006, -0.017, 0.035, -0.029, 0.002]
returns_exxon_mobil = [0.008, 0.015, 0.009, 0.012, 0.003, -0.007, 0.006, 0.005, -0.048, 0.025, -0.012]
returns_apple = [-0.002, 0.007, -0.004, -0.004, 0.002, 0.013, -0.011, 0.017, -0.001, 0.012, 0.006]

corr_gm_ford = calculate_correlation(returns_general_motors, returns_ford)
print('The correlation coefficient between General Motors and Ford is', corr_gm_ford)

# Write code here
corr_gm_em = calculate_correlation(returns_general_motors, returns_exxon_mobil)
print('The correlation coefficient between General Motors and ExxonMobil is', corr_gm_em)

corr_gm_apple = calculate_correlation(returns_general_motors, returns_apple)
print('The correlation coefficient between General Motors and Apple is', corr_gm_apple)

corrcoef_matrix = np.corrcoef([returns_general_motors, returns_ford, returns_exxon_mobil, returns_apple])
print(corrcoef_matrix)
```

```Python
from data import returns_general_motors, returns_ford, returns_exxon_mobil, returns_apple
from math import sqrt
import numpy as np

def calculate_correlation(set_x, set_y):
  # Sum of all values in each dataset
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  # Sum of all squared values in each dataset
  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])

  # Sum of the product of each respective element in each dataset 
  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])

  # Length of dataset
  n = len(set_x)

  # Calculate correlation coefficient
  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator

# Function calls
print('The correlation coefficient between General Motors and Ford is', calculate_correlation(returns_general_motors, returns_ford))
print('The correlation coefficient between General Motors and ExxonMobil is', calculate_correlation(returns_general_motors, returns_exxon_mobil))
print('The correlation coefficient between General Motors and Apple is', calculate_correlation(returns_general_motors, returns_apple))
```

```Python
from utils import calculate_variance, calculate_stddev

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

annual_returns = [0.02, 0.05, -0.04, 0.04, 0.02, -0.02, 0.01, 0.03, 0.05, 0.02]

# Write code here
annual_returns_percentage = [display_as_percentage(r) for r in annual_returns]
print(annual_returns_percentage)

print('The historical annual rates of return are:', ', '.join(annual_returns_percentage))

variance = calculate_variance(annual_returns)
print('The variance of the rates of return is', variance)

stddev = display_as_percentage(calculate_stddev(annual_returns))
print('The standard deviation of the rates of return is', stddev)



```

