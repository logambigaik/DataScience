# Python Linear Regression -Scikit #

This shows Sandra’s lemonade stand’s revenue over its first 12 months of being open.
From eyeballing the graph, what do you think the revenue in month 13 would be?

<img src="https://github.com/user-attachments/assets/84de1a56-6a99-433d-9f34-aecad01044f3" width=350>

```Python
import seaborn
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

month_13 = 0
plt.plot(months, revenue, "o")

plt.title("Sandra's Lemonade Stand")

plt.xlabel("Months")
plt.ylabel("Revenue ($)")

plt.show()

# What do you think the revenue in month 13 would be?
```
A line is determined by its slope and its intercept. In other words, for each point y on a line we can say:

**y=mx+b**
where **m** is the slope, and **b** is the intercept. **y** is a given point on the y-axis, and it corresponds to a given **x** on the x-axis.

The slope is a measure of how steep the line is, while the intercept is a measure of where the line hits the y-axis.

```Python
import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 8
#intercept:
b = 40

# y_values = [slope*x_value + intercept for x_value in x_values]

y = [m*x + b for x in months]
plt.plot(months, revenue, "o")
plt.plot(months, y)


# With different m & b value
# y_values = [slope*x_value + intercept for x_value in x_values]
m =10
b= 42
y = [m*x + b for x in months]
plt.plot(months, y)
plt.show()

```
**Graph**

<img src="https://github.com/user-attachments/assets/ae580d99-90d7-47c3-8e1c-50ad377679ca" width=350>

**Loss**

When we think about how we can assign a slope and intercept to fit a set of points, we have to define what the best fit is.

For each data point, we calculate loss, a number that measures how bad the model’s (in this case, the line’s) prediction was. You may have seen this being referred to as error.

We can think about loss as the squared distance from the point to the line. We do the squared distance (instead of just the distance) so that points above and below the line both contribute to total loss in the same way:

<img src="https://github.com/user-attachments/assets/13de148d-020f-40f1-a227-7508c3dde036" width=350>

In this example:

* For point A, the squared distance is 9 (3²)
* For point B, the squared distance is 1 (1²)
  
So the total loss, with this model, is 10. If we found a line that had less loss than 10, that line would be a better model for this data.

We have three points, (1, 5), (2, 1), and (3, 3). We are trying to find a line that produces lowest loss. As per calculation m2 value matches

```Python
x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 =[m1 * i +b1 for i in x ]
y_predicted2 =[m2 * i +b2 for i in x ]

total_loss1 = 0
for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2

total_loss2 = 0
for i in range(len(y)):
  total_loss2 += (y[i] - y_predicted2[i]) ** 2

print(total_loss1, total_loss2)
better_fit =2

```
**Minimizing Loss**

The goal of a linear regression model is to find the slope and intercept pair that minimizes loss on average across all of the data.

**Gradient Descent for Intercept**
As we try to minimize loss, we take each parameter we are changing, and move it as long as we are decreasing loss. It’s like we are moving down a hill, and stop once we reach the bottom:

<img src='https://github.com/user-attachments/assets/0eb2212a-6470-468c-8ce3-1300e5d75b4c' width=350>

For example, let’s say we are trying to find the intercept for a line. We currently have a guess of 10 for the intercept. At the point of 10 on the curve, the slope is downward. Therefore, if we increase the intercept, we should be lowering the loss. So we follow the gradient downwards.

<img src='https://github.com/user-attachments/assets/2c3a261e-0d6b-42e5-abab-cb85358a0565' width=350>

We derive these gradients using calculus. It is not crucial to understand how we arrive at the gradient equation. To find the gradient of loss as intercept changes, the formula comes out to be:

<img src='https://github.com/user-attachments/assets/e3c47ba1-1e86-4819-8ef8-d04cb3341bd9' width=350>

* N is the number of points we have in our dataset
* m is the current gradient guess
* b is the current intercept guess

Basically:

we find the sum of y_value - (m*x_value + b) for all the y_values and x_values we have and then we multiply the sum by a factor of -2/N. N is the number of points we have.

```Python
def get_gradient_at_b(x, y, m, b):
  diff = 0

  # N is the number of points
  N = len(x)
  
  for i in range(0, len(x)):
    y_val = y[i]
    x_val = x[i]
    diff += (y_val - ((m * x_val) + b))
  
  # Define b_gradient
  b_gradient = -2/N * diff
  return b_gradient
```

**Gradient Descent for Slope**

We have a function to find the gradient of b at every point. To find the m gradient, or the way the loss changes as the slope of our line changes, we can use this formula:

<img src="https://github.com/user-attachments/assets/4e4c390b-e60c-4767-bec6-51cbac485879" width=350>

Once more:

* N is the number of points you have in your dataset
* m is the current gradient guess
* b is the current intercept guess

To find the m gradient:

we find the sum of x_value * (y_value - (m*x_value + b)) for all the y_values and x_values we have and then we multiply the sum by a factor of -2/N. N is the number of points we have.

Once we have a way to calculate both the m gradient and the b gradient, we’ll be able to follow both of those gradients downwards to the point of lowest loss for both the m value and the b value. Then, we’ll have the best m and the best b to fit our data!

```Python
def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += (y_val - ((m * x_val) + b))
    b_gradient = -2/N * diff
    return b_gradient
  
def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val*(y_val - ((m * x_val) + b))
    m_gradient = -2/N * diff
    return m_gradient
```


**Put it Together**

Now that we know how to calculate the gradient, we want to take a “step” in that direction. However, it’s important to think about whether that step is too big or too small. We don’t want to overshoot the minimum error!

We can scale the size of the step by multiplying the gradient by a learning rate.

To find a new b value, we would say: **new_b = current_b - (learning_rate * b_gradient)**

where **current_b** is our guess for what the b value is, **b_gradient** is the gradient of the loss curve at our current guess, and learning_rate is proportional to the size of the step we want to take.

``` Python
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (0.01 * b_gradient)
    m = m_current - (0.01 * m_gradient)
    return [b, m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

b, m = step_gradient(months, revenue, b, m)
print(b, m)
```

**Convergence**

How do we know when we should stop changing the parameters m and b? How will we know when our program has learned enough?

To answer this, we have to define convergence. Convergence is when the loss stops changing (or changes very slowly) when parameters are changed.

``` Python
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01

iterations = range(1400)

num_iterations = 800
convergence_b = 47
plt.plot(iterations, bs)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()
```

**Graph**

<img src='https://github.com/user-attachments/assets/b5925f43-45b1-4b0e-95f8-1519b7c62438' width=350>

**Learning Rate**

We want our program to be able to iteratively learn what the best m and b values are. So for each m and b pair that we guess, we want to move them in the direction of the gradients we’ve calculated. But how far do we move in that direction?

We have to choose a learning rate, which will determine how far down the loss curve we go.

A small learning rate will take a long time to converge — you might run out of time or cycles before getting an answer. A large learning rate might skip over the best value. It might never converge! Oh no!

<img src="https://github.com/user-attachments/assets/d39fbf8f-c84f-4a09-a6af-ae4afdb6e8da" width=350>


Finding the absolute best learning rate is not necessary for training a model. You just have to find a learning rate large enough that gradient descent converges with the efficiency you need, and not so large that convergence never happens.

``` Python
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01

# iterations = range(1400)
iterations = range(100)

plt.plot(iterations, bs_01)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()
```

<img src='https://github.com/user-attachments/assets/8a19438c-b458-422f-9561-bcdd404862c8' width=350>


**Put it together**

``` Python - gradient_descent_funcs.py
import codecademylib3_seaborn
import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#Your gradient_descent function here:  
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return [b,m]  

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()

```

**Graph**

<img src='https://github.com/user-attachments/assets/b387b8ce-b3cb-4a69-8bd4-be3b6066bc24' width=350>


**Test with real data**
```Python
import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]


b, m =gradient_descent(X,y,num_iterations=1000,learning_rate=0.0001)

y_predictions =[m*x + b for x in X]

plt.plot(X, y, 'o')
#plot your line here:
plt.plot(X, y_predictions)
plt.show()
# print(y_predictions)
# print(f"{X}.2f-{y}.2f")

```

**Graph**

<img src='https://github.com/user-attachments/assets/a1da5708-b3d5-4a87-9b80-d1038ae9272d' width=350>


### Scikit-Learn

Luckily, we don’t have to do this every time we want to use linear regression. We can use Python’s scikit-learn library. Scikit-learn, or sklearn, is used specifically for 
Preview: Docs Machine learning is a branch of artificial intelligence that enables systems to learn from data and make predictions or decisions without explicit programming.
Machine Learning
. Inside the linear_model module, there is a LinearRegression() function we can use:

**from sklearn.linear_model import LinearRegression**


You can first create a LinearRegression model, and then fit it to your x and y data:

**line_fitter = LinearRegression()
line_fitter.fit(X, y)**



The .fit() method  gives the model two  variables that are useful to us:

1. the line_fitter.coef_, which contains the slope
2. the line_fitter.intercept_, which contains the intercept

We can also use the .predict() function to pass in x-values and receive the y-values that this line would predict:

**y_predicted = line_fitter.predict(X)**

Note: the num_iterations and the learning_rate that you learned about in your own implementation have default values within scikit-learn,

```Python #Sample Python Code for Scikit-learn
import codecademylib3_seaborn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

plt.plot(temperature, sales, 'o')

#for invoking Linear regression
line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)
sales_predict = line_fitter.predict(temperature)

plt.plot(temperature, sales_predict)
plt.show()

```

**Graph**

<img src='https://github.com/user-attachments/assets/59b8e595-132e-46cf-95de-6d90ca1f676d' width=350>


### Final Review 

1. We can measure how well a line fits by measuring loss.
2. The goal of linear regression is to minimize loss.
3. To find the line of best fit, we try to find the b value (intercept) and the m value (slope) that minimize loss.
4. Convergence refers to when the parameters stop changing with each iteration.
5. Learning rate refers to how much the parameters are changed on each iteration.
6. We can use Scikit-learn’s LinearRegression() model to perform linear regression on a set of points.


**Another example Python code **

``` Python
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# Boston housing dataset
boston = load_boston()

df = pd.DataFrame(boston.data, columns = boston.feature_names)

# Set the x-values to the nitrogen oxide concentration:
X = df[['NOX']]
# Y-values are the prices:
y = boston.target

# Can we do linear regression on this?
line_fitter = LinearRegression()
line_fitter.fit(X, y)
target_predict = line_fitter.predict(X)

plt.scatter(X, y, alpha=0.4)
# Plot line here:
plt.plot(X, target_predict)

plt.title("Boston Housing Dataset")
plt.xlabel("Nitric Oxides Concentration")
plt.ylabel("House Price ($)")
plt.show()
```

**Output-graph**

![image](https://github.com/user-attachments/assets/1a96baf2-9afc-4ffe-a5c8-7e240e68bb82)
