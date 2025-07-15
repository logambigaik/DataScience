# Data Types Interview Questions

Practice answering common interview questions about general data concepts and data types.

---

## Introduction

Hi! My name is Codey Cademy. I’m so excited because today I’m interviewing candidates for the data scientist role on my team. I’m looking for someone who understands all the stages of data science: exploratory analysis, diagnostic analyses, and data organization.

---

## Theoretical Questions

### How do you typically start an exploratory data analysis?

**Answer:**
1. **Understand the context:** Clarify the problem statement, goals, and the source of the dataset.
2. **Inspect the data:** Load the dataset and use `.head()`, `.info()`, and `.describe()` to get a general understanding.
3. **Check for missing values:** Identify missing or null values using `.isnull().sum()`.
4. **Data types:** Ensure that data types are as expected and convert them if needed.
5. **Univariate analysis:** Analyze distributions of individual columns.
6. **Bivariate/multivariate analysis:** Explore relationships using scatter plots, box plots, correlation matrices, etc.
7. **Detect outliers and anomalies.**
8. **Summarize findings:** Identify initial patterns, anomalies, and questions for deeper analysis.

---

### Tell me about a data analytics project you worked on and the major steps you took to complete it.

**Answer:**
I worked on a real estate price prediction project. The steps I took were:
1. **Problem understanding and data acquisition.**
2. **Data cleaning:** Dealt with missing values, removed outliers, and handled data type issues.
3. **EDA:** Performed univariate and multivariate analysis using visualization and statistics.
4. **Feature engineering:** Created new variables and transformed features (e.g., log-transformed price).
5. **Model selection:** Tested various models like linear regression, decision trees, and random forests.
6. **Evaluation:** Used RMSE and cross-validation.
7. **Deployment:** Shared insights via reports and dashboards.

---

## Situational Questions

### E-commerce site: 50% drop in checkouts without customer complaints. How would you diagnose the problem using site data?

**Answer:**
1. **Segment time:** Compare before and after the drop.
2. **Funnel analysis:** Track user paths from landing to checkout.
3. **Clickstream:** Check for broken links, delays, or errors in the checkout page.
4. **Session duration:** Look for changes in user engagement.
5. **A/B test logs:** Ensure no experimental changes caused the issue.
6. **Backend logs:** Check for errors or downtime.
7. **Device/browser split:** Ensure no compatibility issues.

---

### Rideshare startup: What questions would you ask and how would you begin to explore Detroit-area data?

**Answer:**
**Questions:**
- What areas have low car ownership but high insurance premiums?
- Is there a correlation between demographics and vehicle usage?
- Are there patterns in insurance rates over time or by neighborhood?

**Exploration steps:**
1. **Clean the data:** Handle missing values and format date columns.
2. **EDA:** Demographic distribution, vehicle ownership trends.
3. **Mapping:** Use geospatial analysis for regional insights.
4. **Time series:** Analyze trends from 2019 to 2021.
5. **Clustering:** Segment residents for targeted marketing.

---

## Temporal Data

### What is time series analysis, and what aspects would you keep in mind when working with time series?

**Answer:**
Time series analysis involves analyzing data points indexed in time order.
Key aspects:
- **Stationarity:** Constant mean and variance over time.
- **Seasonality:** Periodic patterns.
- **Trend:** Long-term increase or decrease.
- **Noise:** Random variation.
- **Lags and autocorrelation.**
- **Handling missing timestamps.**

---

### Coding: Convert string to timestamp in Python

```python
import pandas as pd

date_str = "2023-07-15"
date_obj = pd.to_datetime(date_str)
print(date_obj)
```

---

### Toy company: How would you account for seasonal variation to determine if ads affected sales?

**Answer:**
1. **Decompose the time series:** Use additive/multiplicative decomposition.
2. **Create a control group:** Compare with regions not exposed to ads.
3. **Use time series models:** Apply ARIMA or seasonal adjustment.
4. **Year-over-year comparison:** Compare sales to same season in previous years.
5. **Interrupted time series analysis.**

---

## Text Data

### What steps would you take to normalize text?

**Answer:**
1. **Lowercasing.**
2. **Removing punctuation and special characters.**
3. **Tokenization.**
4. **Removing stop words.**
5. **Stemming or lemmatization.**
6. **Handling misspellings.**
7. **Removing extra spaces or line breaks.**

---

### Large manufacturing company: How would you process incident reports to identify trends?

**Answer:**
1. **Text cleaning and normalization.**
2. **Named Entity Recognition (NER):** Identify department names, dates, etc.
3. **Text vectorization:** TF-IDF or embeddings.
4. **Topic modeling:** Use LDA or clustering to find common themes.
5. **Trend analysis:** Time-series plotting of incident frequencies.
6. **Data dashboard:** Present insights with visuals and filters.

---

## Review

- Basic data management
- Situational applications
- Temporal and text data strategies




# Data Cleaning Interview Questions

Practice data cleaning and data wrangling interview questions.

---

## 📌 Introduction

In this portion of the interview, we are going to talk about strategies for cleaning data. Data cleaning is a significant part of a data professional’s job — some estimate it takes up to **80% of a data scientist or analyst’s time**!

This section includes:
- **Conceptual questions** asking about your techniques
- **Situational questions** where you describe your approach

---

## 🧠 Conceptual Questions

### ❓ What steps do you take when you first clean a dataset?

1. **Load and inspect** the dataset using `.head()`, `.info()`, and `.describe()`.
2. **Check for missing values** using `.isnull().sum()` or `.isna()`.
3. **Review data types** and convert where necessary (e.g., string to datetime).
4. **Look for duplicates** using `.duplicated()` and drop them if needed.
5. **Standardize string formatting** (trim whitespace, lowercase, etc.).
6. **Handle outliers** through visualizations (boxplots, histograms).
7. **Understand the context** and use domain knowledge to flag suspicious data.

---

### ❓ What data validation methods have you used?

- Cross-checking ranges for numeric fields (e.g., ages between 0–120).
- Regex validation for fields like emails, phone numbers, zip codes.
- Ensuring date sequences are logical (e.g., end date > start date).
- Validating categorical variables against a known set of values.
- Using assertions and test cases in pipelines.

---

### ❓ Do you ever impute data? Why or why not?

Yes, but it depends on:
- **Why data is missing** (Missing Completely at Random vs Not at Random).
- The importance of the feature to model accuracy.
- Common methods:
  - **Mean/median/mode imputation**
  - **Forward/backward fill** for time series
  - **Model-based imputation** (e.g., KNN, regression)
- I always flag imputed values to avoid misleading conclusions.

---

## 💻 Coding Question

**Objective**: Clean missing values from a dataset.

**Dataset Snippet**:

```
Name              Salary    Age Children    Company
Vanna Holland     5738.45   40  5           
Gretchen Kemp     9765.50   53  2           Feugiat Lorem Ipsum Company
Brittany Porter   8557.05   37              Magna Ut Industries
Kaseem Crawford   1424.80   20  4           
Lamar Payne       2442.63   28  5           Amet Incorporated
```

### ✅ Tasks:
- Identify rows with missing values.
- Remove rows with **>2 missing values**.
- For rows with **1 missing value**, replace it with the **median** of the column.
- Add a new column `Imputed` (True/False) indicating if any value was imputed.

### 🧾 Code:

```python
import pandas as pd

# Load dataset
df = pd.read_csv('EmployeeRecords.csv')

# Count missing values per row
df['MissingCount'] = df.isnull().sum(axis=1)

# Create Imputed column
df['Imputed'] = False

# Remove rows with >2 missing values
df = df[df['MissingCount'] <= 2]

# Impute single missing values with median
for col in ['Salary', 'Age', 'Children']:
    median_val = df[col].median()
    mask = df[col].isnull()
    df.loc[mask, col] = median_val
    df.loc[mask, 'Imputed'] = True

# Drop helper column
df = df.drop(columns=['MissingCount'])

# Final cleaned dataset
print(df.head())
```

---

## 🧩 Situational Questions

### 🏥 Healthcare Company:

> We have millions of anonymized records, but many appointment notes are missing. We want to explore the relationship between time nurses spend with patients and complaint categories.

**Response**:
- First, assess the **percentage and pattern of missing notes**.
- Use other available fields (e.g., complaint codes, duration, diagnosis) to infer or cluster note patterns.
- Consider **Natural Language Processing** to evaluate partial notes.
- Avoid imputing text if notes are critical for interpretation — better to:
  - Flag those records
  - Perform analysis separately with and without them
  - Investigate why the notes are missing (systemic error?)

---

### 🧠 Non-Profit Organization:

> We're conducting a survey about policing attitudes. How would you determine if some responses were filled at random?

**Response**:
- Look for **straight-lining** (same response for every question).
- Identify unusually **fast completion times**.
- Check for **inconsistencies** (e.g., contradictory answers).
- Use statistical techniques like:
  - Response pattern clustering
  - Mahalanobis distance for outlier detection
- Compare to control group or benchmark answers.

---

## ✅ Review Summary


- Techniques for **dealing with missing data**
- When and how to **impute values**
- Practical **data validation**
- Situational judgment in **real-world data wrangling**

---

> “Data cleaning might not be glamorous, but it’s where true insights begin.”  
> — Every real data scientist, ever.


### Summary Statistics interview questions

```python
import pandas as pd

df = pd.read_csv('avocado.csv')
print(df.head(5))
print(df.columns)

avg_price =df['AveragePrice'].mean()
print(avg_price)
med_price = df['AveragePrice'].median()
print(med_price)
```
# What does avg_price mean?
avg_price_explanation = """
The variable 'avg_price' represents the average (arithmetic mean) price of avocados 
from all the entries in the dataset. It is calculated by summing all the values in 
the 'AveragePrice' column and dividing by the number of entries.
"""

# Why are the mean and the median different?
mean_vs_median_explanation = """
The mean and the median are different because the distribution of avocado prices may 
not be symmetrical. If there are outliers or a skew in the data (e.g., a few very high 
or very low prices), they can pull the mean away from the median. The median, being 
the middle value when the data is sorted, is less affected by extreme values.
"""

# When would you report the median instead of the mean?
when_to_use_median_explanation = """
You would report the median instead of the mean when the data is skewed or contains 
outliers. The median provides a better representation of the 'typical' value in such 
cases, as it is not influenced by extremely high or low values that could distort the mean.
"""

print(avg_price_explanation)
print(mean_vs_median_explanation)
print(when_to_use_median_explanation)


# Measures of Spread: Avocado Price and Volume Analysis

In this analysis, we are exploring the spread (range) of two main variables in the avocado dataset:
- `AveragePrice`: The daily average price of avocados.
- `Total Volume`: The estimated number of avocados sold (which may include fractional values across multiple cities).

---

## 🔢 Code

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('avocado.csv')
print(df.head())

# Get the list of column names
my_columns = list(df.columns)
print(my_columns)

# Maximum and minimum Total Volume
max_vol = df["Total Volume"].max()
min_vol = df["Total Volume"].min()
print(max_vol, min_vol)

# Range of Total Volume
range_vol = max_vol - min_vol
print(range_vol)

# Maximum and minimum Average Price
max_price = df["AveragePrice"].max()
min_price = df["AveragePrice"].min()
print(max_price, min_price)

# Range of Average Price
range_price = max_price - min_price
print(range_price)
```

#### Hint 

* On the cheapest day for avocados, they sold for just 44 cents. On the most expensive day, they were $3.25. That’s a $2.81 range in avocado prices.

* Only 85 avocados were sold on the day with the fewest avocado sales. On the day with the most avocado sales, 62,505,647 avocados were sold.
This means that there was a range of 62,505,562 avocados!


#### Histogram

* The daily price of avocados is normally distributed, and the daily total volume sold is right-skewed. This means that there are many more days when there were just a few avocado sales versus days with lots of sales.

```python
import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avocado.csv')
print(df.head())

max_vol = df["Total Volume"].max()
min_vol = df["Total Volume"].min()
max_price = df.AveragePrice.max()
min_price = df.AveragePrice.min()

plt.hist(df.AveragePrice, range=(0, 3.5), bins=14)
plt.show()
```


#### Interquartile Range

* While range is a very common statistic to report, so is interquartile range. In this exercise, we will investigate the interquartile range of the two variables

    * AveragePrice
    * Total Volume
 
```python
import numpy as np
import pandas as pd
from scipy.stats import iqr

df = pd.read_csv("avocado.csv")

print(df.head())

iqr_price = iqr(df['AveragePrice'])
print(iqr_price)

iqr_vol = iqr(df['Total Volume'])
print(iqr_vol)

"""The interquartile range for the price is just 56 cents. This means that the majority of avocados, or the middle 50% of avocadoes were sold within 56 cents of each other"""

"""The middle 50% of total volume of daily sales was within 422,123. The fact that this is so much smaller than 62,000,000 demonstrates that there is a huge range in the top quartile, incidating some outlier days for the sale of avocados"""
```

#### Association between Variables
In this final exercise, we’d like you to determine if there is an association between AveragePrice and Total Volume.

If we lower the price of avocados, do people also purchase fewer of them? You do not need to determine if there is a causal relationship between the variables, but you should be able to determine if there is an association.

```python
import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr


df = pd.read_csv("avocado.csv")

# create your scatter plot here:
plt.scatter(df['AveragePrice'], df['Total Volume'])
plt.xlabel('Average Daily Price')
plt.ylabel('Total Daily Sales')
plt.show()

# calculate corr_sqfeet_beds and print it out:
corr_price_vol, p = pearsonr(df['AveragePrice'], df['Total Volume'])
print(corr_price_vol)

"""The Pearson correlation coefficient is approximately -.19. This is very low, and indicates no linear relationship between these variables. The scatterplot of Price versus sales shows two distinct clusters. It may be worth investigating these clusters independently in another round of evaluation."""
```

<img width="600" height="682" alt="image" src="https://github.com/user-attachments/assets/2abdc05b-de7b-460c-84eb-8145d7cd771d" />


