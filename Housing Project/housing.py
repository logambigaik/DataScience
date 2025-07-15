import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load in housing data
housing_data = pd.read_csv('housing_data.csv')

# check the columns
housing_data.columns

# descriptive statistics summary
housing_data['SalePrice'].describe()

# histogram
sns.displot(housing_data['SalePrice'])
plt.show()
plt.clf()

# perform log transformation on sale price data
log_data = np.log(housing_data['SalePrice'])
print(log_data.skew())
sns.displot(log_data)
plt.show()
plt.clf()

# visualize relationship between 1st floor sq feet and sale price
data = pd.concat([housing_data['SalePrice'], housing_data['1stFlrSF']], axis=1)
data.plot.scatter(x='1stFlrSF', y='SalePrice', ylim=(0,800000))
plt.show()
plt.clf()

# visualize relationship between garage area and sale price
data = pd.concat([housing_data['SalePrice'], housing_data['GarageArea']], axis=1)
data.plot.scatter(x='GarageArea', y='SalePrice', ylim=(0,800000))
plt.show()
plt.clf()

# visualize relationship between year built and sale price
data = pd.concat([housing_data['SalePrice'], housing_data['YearBuilt']], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x='YearBuilt', y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
plt.show()
plt.clf()
