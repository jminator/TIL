import Ch2_4_select_and_train_a_model as st
import Ch2_3_transformation_pipeline as tp
import Ch2_1_create_datasets as cd
housing_prepared = st.housing_prepared.copy()
housing_labels = st.housing_labels.copy()
import numpy as np
import scipy.stats as stats

# There are many ways to fine-tune the models
# 1. Grid search
# 2. Randomized search
# 3. Ensemble method

## GRID SEARCH ##
# tries out all possible combinations of hyperparameter values

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]}, 
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]} 
] 
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv = 3,
                            scoring= 'neg_mean_squared_error', 
                            return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)

# when not sure about hyperparameter values, try out consecutive powers of 10 or a smaller number
# the param_grid will first try out 3x4 combinations,
# then try another 2x3 with bootstrap off
# grid_search will train each model 5 times. => 18x5=90 rounds of training

grid_search.best_params_ # would give the best combination
grid_search.best_estimator_ # get the best estimator directly


# evaluation scores are also available

# cvres = grid_search.cv_results_
# for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
#     print(np.sqrt(-mean_score), params)

# also, we can treat some of the data preparation steps as hyperparameters.
# grid search can automatically find out whether or not to add a feature you were not sure about

## RANDOM SEARCH ##
# when the hyperparameter search space is large, random search is preferable
# it evaluates a given number of random combinations by selecting a random value for each hyperparameter
# at every iteration. there are two main benefits for this method:
# 1) if you let the r.search for 1000 iterations, it will explore 1000 different values for each parameter
# instead of just a few values per hyperp. with the grid search approach
# 2) you have more control over the computing budget you wan to allocate to hyperp. search.

from sklearn.model_selection import RandomizedSearchCV
forest_reg = RandomForestRegressor()

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]

# Number of features to consider at every split
max_features = ['auto', 'sqrt']

# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)

# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]

# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]

# Method of selecting samples for training each tree
bootstrap = [True, False]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

# rand_search = RandomizedSearchCV(forest_reg, param_distributions = random_grid, cv = 3,
#                             n_iter = 10, random_state=42, 
#                             scoring= 'neg_mean_squared_error', 
#                             return_train_score=True,)
# rand_search.fit(housing_prepared, housing_labels)
# rand_search.best_params_

# Analyze the best models and their errors
feature_importances = grid_search.best_estimator_.feature_importances_
extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
cat_encoder = tp.full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs = list(cat_encoder.categories_[0])
attributes = tp.num_attribs + extra_attribs + cat_one_hot_attribs
# print(sorted(zip(feature_importances, attributes), reverse=True))
# with this info, may want to drop some of the less useful features


## EVALUATE YOUR SYSTEM ON THE TEST SET ##
final_model = grid_search.best_estimator_
X_test = cd.strat_test_set.drop("median_house_value", axis = 1)
y_test = cd.strat_test_set["median_house_value"].copy()


