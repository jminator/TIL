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

# Looking for correlations
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False) # gives numerical values

from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms",
    "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))
plt.show()

# Experimenting with Attribute Combinations
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["household"]