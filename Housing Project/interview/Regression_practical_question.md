```python
import codecademylib3
import pandas as pd
import numpy as np

df = pd.read_csv("wine_ratings.csv")

print(df.head())
print(df.describe())
print(df.columns)
print(df.dtypes)
print(df.nunique())
print(df.corr())

"""This is a relatively clean dataset! It looks like all of the variables are continuous and formatted as floats except for category which is a string. There is a unique identifier column that I will be sure not to include in the model. """
```

#### Single Linear Regression
```python
import codecademylib3
import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("wine_ratings.csv")

#reshape the predictor (alcohol) and target (rating) values.
alcohol = df['alcohol'].values.reshape(-1,1)
rating = df['rating'].values.reshape(-1,1)

#create a linear regression model fitted to the alcohol feature.
lr_alcohol = LinearRegression()
lr_alcohol.fit(alcohol, rating)

#predict the ratings based on the alcohol model
rating_predict_alcohol = lr_alcohol.predict(alcohol)
df['alcohol_predict'] = rating_predict_alcohol

#plot the alcohol versus the real ratings and the alcohol versus the predicted ratings on the same plot
plt.plot(alcohol, rating, 'o')
plt.plot(alcohol, rating_predict_alcohol)
plt.show()

#calculate the R^2 score
alcohol_r2 = lr_alcohol.score(alcohol, rating)
print(alcohol_r2)

"""The R^2 value is very low, suggesting that the model does not fit the data well. Since R^2 is on a scale of 0 to 1 and this model is less than .2, it is not a good fit for the existing data. That is, the difference between the real and predicted values are very high."""

#calculate the alcohol residuals
df['alcohol_residuals'] = abs(df['rating']) - abs(df['alcohol_predict'])

#make a qq plot of the residuals to test normalcy
fig = sm.qqplot(df['alcohol_residuals'] , stats.t, fit=True, line="45")
plt.show()
```
"""The residuals are close to normally distributed, which fulfills our assumptions about normality. Likewise, the data seems linear even though the model is not a particularly good fit. So I will not transform the alcohol variable."""


### Multiple Linear Regression

```python
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("wine_ratings.csv")
print(df.head())

#separate data from labels
data = df.drop(['category','uuid', 'rating'], axis=1)
label = df['rating']

#scale data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

#split into training and testing
x_train, x_test, y_train, y_test = train_test_split(data_scaled, label, train_size=0.8, test_size=0.2)

# fit a multiple linear regression model
mlr = LinearRegression()
mlr.fit(x_train, y_train)

#make predictions based on that model
y_predict = mlr.predict(x_test)

#create scatter plot of predictions vs. actual ratings
plt.scatter(y_test, y_predict, alpha=0.4)
plt.show()

#print the coefficients and max coefficient
mlr_coef = mlr.coef_
print(mlr_coef)

#print the maximum coefficient
print("The max coefficient is: ",np.max(mlr_coef))

#find the index of the maximum coefficient
max_coef_index = np.argmax(mlr_coef)
#make a list of the columns in the dataset
column_name_list = data.columns.tolist()
#use the index of the max coefficient to find the feature with the maximum coefficient
print("The feature with the max coefficient is: ", column_name_list[max_coef_index])

print("The R^2 score is: ",r2_score(y_test, y_predict))

"""None of the predictor variables are very good predictors. Alcohol contributes the most to the model, but it is still a very weak predictor. The R^2 value shows that the model does not fit the data very closely as it is very low (less than .3)"""

df_corr = df.corr()
print(df_corr)

#that's hard to read, so use the unstack and sort method
df_corr_list = df_corr.unstack()
df_corr_rank = df_corr_list.sort_values(ascending = False)

#print starting at 13 to exclude self-correlations
print(df_corr_rank[13:30])
```

"""The sulfur dioxide variables are highly correlated. We can remove one of those to see if the model will become more robust. Density and residual sugar also seem to be highly correlated, but not strongly enough to warrant removing them."""

#### Improved Multiple Linear Regression
```python
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("wine_ratings.csv")
print(df.head())

#change category to 'red'
df['category'].replace(['red','white'],[1,0], inplace=True)
df.rename({'category':'red'}, axis=1, inplace=True)

df_selected = df.drop(['uuid',  'total sulfur dioxide'], axis=1)

"""I changed 'category' to a binary variable to be able to use it in the model. I also dropped the uuid and total sulfur dioxide because it was highly correlated with free sulfur dioxide"""

data = df_selected.drop(['rating'], axis=1)
label = df_selected['rating']

#scale data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

x_train, x_test, y_train, y_test = train_test_split(data_scaled, label, train_size=0.8, test_size=0.2)

mlr = LinearRegression()
mlr.fit(x_train, y_train) 
y_predict = mlr.predict(x_test)

plt.scatter(y_test, y_predict, alpha=0.4)
plt.show()
print(r2_score(y_test, y_predict))
```

"""Removing the total sulfur dioxide and adding the wine type variable actually degraded the model. I would like to try to make 2 more versions: one with just the category removed and one with just the total free sulfide removed. It appears that the total free sulfide may have contributed slightly to the model. However, no matter what, the model does not fit the data very well and is not a good predictor of the rating. """

