# Python Linear Regression purpose ###
--- 
This shows Sandra’s lemonade stand’s revenue over its first 12 months of being open.
From eyeballing the graph, what do you think the revenue in month 13 would be?
---

```Python
import codecademylib3_seaborn
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
