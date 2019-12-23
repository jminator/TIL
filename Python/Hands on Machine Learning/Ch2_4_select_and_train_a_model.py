import Ch2_3_transformation_pipeline as tp
import Ch2_2_explore_data as ed
housing = tp.housing.copy()
housing_prepared = tp.housing_prepared.copy()
housing_labels = ed.housing_labels.copy() # the observed values

## LINEAR REGRESSION ##
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

# now test it with some data from the training set
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5] # the actual values
some_data_prepared = tp.full_pipeline.transform(some_data)
# print("predictions: ", lin_reg.predict(some_data_prepared))
# print("labels: ", list(some_labels))
# we can see that the prediction is not exactly accurate

# we can measure the model's RMSE on the whole training set using mean_squared_error()
from sklearn.metrics import mean_squared_error
import numpy as np

housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
# print(lin_rmse) # the model is underfitting

# Since linear regression model isn't very good, we can try another model


## DECISION TREE ##
# capable of finding complex nonlinear relationship in the data
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)

# now let's evaluate
housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
# print(tree_rmse) # gives 0. means the model must be overfitting.


## CREATING VALIDATION SET ##
# use scikit-learn's 'k-fold cross validation' feature
# this randomly splits the training set into 10 distinct subsets called 'folds',
# then it trains and evaluated the decision tree model 10 times

from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring ="neg_mean_squared_error", cv = 10)
tree_rmse_scores = np.sqrt(-scores)
# note that the cv feature expect a utility function(greater is better) rather than a cost function(smaller the better)
# so the scoring function is actually the opposite of the MSE(i.e the negative value),
# which is why the code computes '-score' before calculating the square root.

def display_scores(scores):
    print("Scores: ", scores.round(2))
    print("Mean: ", scores.mean().round(2))
    print("Std: ", scores.std().round(2))

# display_scores(tree_rmse_scores)
# It shows that the decision tree regressor is not doing well either.


## RANDOM FOREST REGRESSOR ##
# Uses many decision trees on random subsets of the features, then average out their predictions.
# Ensemble learning: building a model on top of many other models.

# from sklearn.ensemble import RandomForestRegressor
# forest_reg = RandomForestRegressor()
# forest_reg.fit(housing_prepared, housing_labels)
# scores = cross_val_score(forest_reg, housing_prepared, housing_labels, scoring ="neg_mean_squared_error", cv = 10)
# forest_rmse_scores = np.sqrt(-scores)
# display_scores(forest_rmse_scores)