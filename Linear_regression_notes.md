# Python Linear Regression purpose ###

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

N is the number of points we have in our dataset
m is the current gradient guess
b is the current intercept guess
Basically:

we find the sum of y_value - (m*x_value + b) for all the y_values and x_values we have
and then we multiply the sum by a factor of -2/N. N is the number of points we have.


