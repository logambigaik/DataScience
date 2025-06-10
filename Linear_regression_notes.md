# Python Linear Regression purpose ###

This shows Sandra’s lemonade stand’s revenue over its first 12 months of being open.
From eyeballing the graph, what do you think the revenue in month 13 would be?
![image](https://github.com/user-attachments/assets/84de1a56-6a99-433d-9f34-aecad01044f3)

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
![image](https://github.com/user-attachments/assets/ae580d99-90d7-47c3-8e1c-50ad377679ca)

