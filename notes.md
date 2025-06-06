### Side-by-Side Box Plots
The difference in mean math scores for students at GP and MS was 0.64. How do we know whether this difference is considered small or large? To answer this question, we need to know something about the spread of the data.

One way to get a better sense of spread is by looking at a visual representation of the data. Side-by-side box plots are useful in visualizing mean and median differences because they allow us to visually estimate the variation in the data. This can help us determine if mean or median differences are “large” or “small”.

Let’s take a look at side by side boxplots of math scores at each school:

sns.boxplot(data = df, x = 'school', y = 'G3')
plt.show()


Looking at the plot, we can clearly see that there is a lot of overlap between the boxes (i.e. the middle 50% of the data). Therefore, we can be more confident that there is not much difference between the math scores of the two groups.

In contrast, suppose we saw the following plot:
In this version, the boxes barely overlap, demonstrating that the middle 50% of scores are different for the two schools. This would be evidence of a stronger association between school and math score.

import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
import seaborn as sns

students = pd.read_csv('students.csv')

#create the boxplot here:
sns.boxplot(data=students, x ='address',y='G3')

plt.show()


Inspecting Overlapping Histograms
=================================
Another way to explore the relationship between a quantitative and categorical variable in more detail is by inspecting overlapping histograms. In the code below, setting alpha = .5 ensures that the histograms are see-through enough that we can see both of them at once. We have also used normed=True make sure that the y-axis is a density rather than a frequency (note: the newest version of matplotlib renamed this parameter density instead of normed):

plt.hist(scores_GP , color="blue", label="GP", normed=True, alpha=0.5)
plt.hist(scores_MS , color="red", label="MS", normed=True, alpha=0.5)
plt.legend()
plt.show()

By inspecting this histogram, we can clearly see that the entire distribution of scores at GP (not just the mean or median) appears slightly shifted to the right (higher) compared to the scores at MS. However, there is also still a lot of overlap between the scores, suggesting that the association is relatively weak.

Note that there are only 46 students at MS, but there are 349 students at GP. If we hadn’t used normed = True, our histogram would have looked like this, making it impossible to compare the distributions fairly:
While overlapping histograms and side by side boxplots can convey similar information, histograms give us more detail and can be useful in spotting patterns that were not visible in a box plot (eg., a bimodal distribution). For example, the following set of box plots and overlapping histograms illustrate the same hypothetical data:


While the box plots and means/medians appear similar, the overlapping histograms illuminate the differences between these two distributions of scores.


import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#create the overlapping histograms here:
plt.hist(scores_urban, color="blue", label="Urban", normed=True, alpha=0.5)
plt.hist(scores_rural, color="red", label="Rural", normed=True, alpha=0.5)
plt.legend()
plt.show()

**Exploring Non-Binary Categorical Variables**
==============================================
In each of the previous exercises, we assessed whether there was an association between a quantitative variable (math scores) and a BINARY categorical variable (school). The categorical variable is considered binary because there are only two available options, either MS or GP. However, sometimes we are interested in an association between a quantitative variable and non-binary categorical variable. Non-binary categorical have more than two categories.

When looking at an association between a quantitative variable and a non-binary categorical variable, we must examine all pair-wise differences. For example, suppose we want to know whether or not an association exists between math scores (G3) and (Mjob), a categorical variable representing the mother’s job. This variable has five possible categories: at_home, health, services, teacher, or other. There are actually 10 different comparisons that we can make. For example, we can compare scores for students whose mothers work at_home or in health; at_home or other; at home or `services; etc.. The easiest way to quickly visualize these comparisons is with side-by-side box plots:

sns.boxplot(data = df, x = 'Mjob', y = 'G3')
plt.show()


Visually, we need to compare each box to every other box. While most of these boxes overlap with each other, there are some pairs for which there are some apparent differences. For example, scores appear to be higher among students with mothers working in health than among students with mothers working at home or in an “other” job. If there are ANY pairwise differences, we can say that the variables are associated; however, it is more useful to specifically report which groups are different.

**Code**

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3

students = pd.read_csv('students.csv')

#create the box-plot here:
sns.boxplot(data=students, x='Fjob', y='G3')

plt.show()

![image](https://github.com/user-attachments/assets/934129f5-2285-4f88-898f-96eb5e945e78)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3

titanic = pd.read_csv('titanic.csv')

Survived = titanic.Fare[titanic.Survived == 1]
Dies = titanic.Fare[titanic.Survived == 0]

survive_mean = np.mean(Survived)
died_mean = np.mean(Dies)

diff_mean = survive_mean-died_mean

print(diff_mean)

survive_med= np.median(Survived)
died_med = np.median(Dies)

diff_med = survive_med-died_med

print(diff_med)

sns.boxplot(data = titanic, x = 'Survived', y = 'Fare')
plt.show()


![image](https://github.com/user-attachments/assets/df870153-d294-4438-94c1-8e05dbc9c1a0)


import pandas as pd
import codecademylib3

housing = pd.read_csv('housing_sample.csv')
#print the first 10 rows of data:
print(housing.head(10))


**Scatter Plots**
===========================
One of the best ways to quickly visualize the relationship between quantitative variables is to plot them against each other in a scatter plot. This makes it easy to look for patterns or trends in the data. Let’s start by plotting the area of a rental against its monthly price to see if we can spot any patterns.

plt.scatter(x = housing.price, y = housing.sqfeet)
plt.xlabel('Rental Price (USD)')
plt.ylabel('Area (Square Feet)')
plt.show()

![image](https://github.com/user-attachments/assets/5f69a4dc-afa8-4da0-9380-f76209351b6e)


This image shows a scatter plot with price on the x-axis and area on the y-axis. There is a clear linear relationship; rentals that cost more tend to have larger area.

While there’s a lot of variation in the data, it seems like more expensive housing tends to come with slightly more space. This suggests an association between these two variables.

It’s important to note that different kinds of associations can lead to different patterns in a scatter plot. For example, the following plot shows the relationship between the age of a child in months and their weight in pounds. We can see that older children tend to weigh more but that the growth rate starts leveling off after 36 months:

Plot showing the relationship between the age of a child in months and their weight in pounds. We can see that older children tend to weigh more but that the growth rate starts leveling off after 36 months

If we don’t see any patterns in a scatter plot, we can probably guess that the variables are not associated. For example, a scatter plot like this would suggest no association:

Scatter plot with no apparent pattern; the points appear randomly distributed.
![image](https://github.com/user-attachments/assets/fdeff416-51b3-416d-8e55-50cfea638cfc)


import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x=housing.beds, y=housing.sqfeet)
plt.xlabel('Number of beds')
plt.ylabel('Number of sqfeet')
plt.show()

![image](https://github.com/user-attachments/assets/27853e06-d4bb-4bb7-8933-2f7e5188901b)
![image](https://github.com/user-attachments/assets/5176105a-38bd-4f85-af61-b37d15782577)


**Exploring Covariance**
=========================
Beyond visualizing relationships, we can also use summary statistics to quantify the strength of certain associations. Covariance is a summary statistic that describes the strength of a linear relationship. A linear relationship is one where a straight line would best describe the pattern of points in a scatter plot.

Covariance can range from negative infinity to positive infinity. A positive covariance indicates that a larger value of one variable is associated with a larger value of the other. A negative covariance indicates a larger value of one variable is associated with a smaller value of the other. A covariance of 0 indicates no linear relationship. Here are some examples:

This figure shows three different plots. In the first, the points are almost exactly along a line with a positive slope and the label is "large positive covariance". In the middle plot, the points are randomly scattered and the label is "covariance of zero". In the last plot, the points are almost exactly on a negatively sloping line and the label is "large negative covariance"

To calculate covariance, we can use the cov() function from NumPy, which produces a covariance matrix for two or more variables
. A covariance matrix for two variables looks something like this:

variable 1	variable 2
variable 1	variance(variable 1)	covariance
variable 2	covariance	variance(variable 2)
In python, we can calculate this matrix as follows:

**cov_mat_price_sqfeet = np.cov(housing.price, housing.sqfeet)
print(cov_mat_price_sqfeet)**
#output: 
[[184332.9  57336.2]
 [ 57336.2 122045.2]]


Notice that the covariance appears twice in this matrix and is equal to 57336.2.

import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision = 1) 

housing = pd.read_csv('housing_sample.csv')

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.sqfeet,housing.beds)

# store the covariance as cov_sqfeet_beds
print(cov_mat_sqfeet_beds)
cov_sqfeet_beds =  228.2

**Output:**
[[110669.     228.2]
 [   228.2      0.7]]


**Correlation- Part 1**
=========================

Like covariance, Pearson Correlation (often referred to simply as “correlation”) is a scaled form of covariance. It also measures the strength of a linear relationship, but ranges from -1 to +1, making it more interpretable.

Highly associated 
Preview: Docs Loading link description
variables
 with a positive linear relationship will have a correlation close to 1. Highly associated variables with a negative linear relationship will have a correlation close to -1. Variables that do not have a linear association (or a linear association with a slope of zero) will have correlations close to 0.

This figure shows 5 different plots. From left to right, the plots show a correlation of 1, a large positive correlation, no correlation, a large negative correlation, and a correlation of -1.)

The pearsonr() function from scipy.stats can be used to calculate correlation as follows:

from scipy.stats import pearsonr
corr_price_sqfeet, p = pearsonr(housing.price, housing.sqfeet)
print(corr_price_sqfeet) #output: 0.507


Generally, a correlation larger than about .3 indicates a linear association. A correlation greater than about .6 suggestions a strong linear association.




**Lambda Functions**
-----------------------------------------

Learn about Lambda Functions in Python!

Python is known for its simplicity and readability, and one of its powerful features is the ability to create functions. While you’re probably familiar with defining functions using the def keyword, Python also offers a more concise way to create small, anonymous functions called lambda functions.

In this article, we’ll dive into the world of lambda functions, exploring their syntax, use cases, and best practices. By the end, you’ll have a solid understanding of how to leverage these compact functions in your Python code.

What are Lambda Functions?
Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of arguments but only one expression. They are defined using the lambda keyword and are typically used for short, simple operations.

Unlike regular functions defined with def, lambda functions don’t have a name and are usually used in situations where you need a simple function for a short period of time.

Let’s compare a regular function with a lambda function:


# Regular function 

def square(x): 

    return x ** 2 

  

# Lambda function 

square_lambda = lambda x: x ** 2 

Both functions square the input, but the lambda function is more concise.

Syntax of Lambda Functions
The basic syntax of a lambda function is:


lambda [arguments]: [expression] 

Here are a couple of simple examples:


# Lambda function to add two numbers 

add = lambda a, b: a + b 

print(add(3, 5))  # Output: 8 

  

# Lambda function to print a name 

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Alice"))  # Output: Hello, Alice! 

Using Lambda Functions
Lambda functions are most commonly used as arguments to higher-order functions such as map(), filter(), and sorted(). Higher-order functions are functions that can accept other functions, such as lambda functions, as arguments. Let’s look at some examples:

Using Lambda with map()
The map() function applies the given lambda function to each item in a list:


numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 

In this example, the lambda function lambda x: x ** 2 squares each number in the numbers list. The map() function applies this lambda to each element, resulting in a new list where every number is squared.

Using Lambda with filter()
The filter() function creates a new list of elements for which the given lambda function returns True:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 

Here, the lambda function lambda x: x % 2 == 0 checks if a number is even. The filter() function uses this lambda to keep only the even numbers from the original list, creating a new list containing only even numbers.

Using Lambda with sorted()
The sorted() function can use a lambda function as a key for custom sorting:


students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 

sorted_students = sorted(students, key=lambda x: x[2]) 

print(sorted_students) 

**Output**: 
[('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 

In this case, the lambda function lambda x: x[2] is used as the key for sorting. It tells the sorted() function to use the third element (index 2) of each tuple for comparison. As a result, the list of students is sorted based on their age (the third element in each tuple).

We’ll further discuss the higher-order functions, such as the map() function, in more detail in our next article.

Advantages and Limitations
Lambda functions offer several advantages:

They are concise and can make code more readable for simple operations.

They’re convenient for small, throwaway functions, especially as arguments to higher-order functions.

However, they also have limitations:

They can only contain expressions, not statements.

They are limited to a single expression, which can make complex operations difficult.

They can be harder to debug due to their anonymous nature.


Use lambda functions when:

You need a simple function for a short period.

You’re passing a simple function as an argument to higher-order functions.

Avoid lambda functions when:

The operation is complex or requires multiple expressions.

You need to reuse the function multiple times (define a regular function instead).

When lambda functions become too complex, it’s often better to use a regular function defined with def. This improves readability and makes your code easier to maintain.

Wrapping Up
Lambda functions are a powerful feature in Python that allow you to write more concise and functional code. They’re particularly useful for simple operations and as arguments to higher-order functions. However, it’s important to use them judiciously and switch to regular functions when the logic becomes more complex.


# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to filter out odd numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Use a lambda function to square each number
squares = list(map(lambda x: x ** 2, numbers))

# Print the results
print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)

# Try creating your own lambda function!
# Uncomment and modify the line below:
# your_result = list(map(lambda x: # Your lambda function here, numbers))
# print("Your result:", your_result)
