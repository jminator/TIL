import Ch2_1_create_datasets as cd
import matplotlib.pyplot as plt

housing = cd.strat_train_set.copy()

# housing.plot(kind="scatter", x="longitude", y="latitude", alpha = 0.1) 
# the alpha option gives different densities to points

# Colour(option c) represents the price, the radius of each circle(coption z) represents the population
# use predefined color map(option cmap) called 'jet'(blue=lower, red=higher)
housing.plot(kind="scatter", x="longitude", y="latitude", alpha = 0.4,
    s = housing["population"]/100, label="population", figsize=(10,7),
    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)

## LOOKING FOR CORRELATIONS ##
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False) # gives numerical values

from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms",
    "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))
# plt.show()

## EXPERIMENTING WITH ATTRIBUTE COMBINATIONS ##
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["households"]
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

## PREPARE THE DATA FOR MACHINE LEARNING ##
housing = cd.strat_train_set.drop("median_house_value", axis = 1) 
# drop: creates a copy of the data without affecting strat_train_set
housing_labels = cd.strat_train_set["median_house_value"].copy()

## DATA CLEANING ##

# 3 options for cleaning out missing values:
# 1. get rid of the entry
# 2. get rid of the whole attribute
# 3. set the values to some value (mean, zero, median, etc)

# housing.dropna(subset=["total_bedrooms"]) # option 1
# housing.drop("total_bedrooms",axis = 1) # option 2
# median = housing["total_bedrooms"].median()
# housing["total_bedrooms"].fillna(median, inplace=True) # option 3

# or we can use sklearn's simpleimputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis = 1) # since median can be computed on numerical variables
imputer.fit(housing_num)
# the imputer stores the median values in its statistics_ instance variable
print(imputer.statistics_)
# now we can use the 'trained' imputer to transform the training set by replacing missing values with the learned medians:
X = imputer.transform(housing_num)


## HANDLING TEXT AND CATEGORICAL ATTRIBUTES ##
# print(housing.info())
housing_cat = housing[["ocean_proximity"]]
# convert texts into numbers
# from sklearn.preprocessing import OrdinalEncoder
# ordinal_encoder = OrdinalEncoder()
# housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
housing_cat_1hot.toarray()
print(cat_encoder.categories_)