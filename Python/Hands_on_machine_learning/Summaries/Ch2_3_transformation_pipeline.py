import Ch2_2_explore_data as ed

housing_num = ed.housing_num.copy()
housing = ed.housing.copy()

# Scikit-learn provides the 'pipeline' class to help with sequences of transformation
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
    ('imputer', ed.SimpleImputer(strategy = "median")),
    ('attribs_adder', ed.CombinedAttributesAdder()),
    ('std_scaler', StandardScaler())
])

housing_num_tr = num_pipeline.fit_transform(housing_num)

# It'd be more convenient to have a single transformer able to handle all columns(not continous, discrete separately)
# we can use ColumnTransformer for this purpose
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

num_attribs = list(housing_num) # gives the list of columns of housing_num
cat_attribs = ["ocean_proximity"]
full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs)
])
housing_prepared = full_pipeline.fit_transform(housing)
