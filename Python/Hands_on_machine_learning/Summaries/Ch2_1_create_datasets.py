import numpy as np
import os
import pandas as pd
import tarfile
from six.moves import urllib
import matplotlib.pyplot as plt

# Download the data

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

fetch_housing_data()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()

# print(housing.head())
# print(housing.info())
# print(housing["ocean_proximity"].value_counts())
# print(housing.describe())

# housing.hist(bins=50, figsize=(20,15))
# plt.show()

# Create a test set: 20% of the entire data

np.random.seed(42)
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
train_set, test_set = split_train_test(housing, 0.2)
# print(len(train_set))
# print(len(test_set))
# print(train_set.head())

# However, the above method will break the next time an updated dataset is fetched.
# Possible solutions:

# 1. Compute a hash of each instance's identifier, put the instance in the test set
# if the hash is lower than or equal to 20% of the maximum hash value.
from zlib import crc32
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2 ** 32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_,test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]
housing_with_id = housing.reset_index()  # adds an 'index' column
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

# To use the row index as an identifier, need to make sure that new data appends to
# the end of the dataset & no row ever gets deleted.

# 2. Use some other distinct identifier eg) latitude and longitude
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

# 3. Use train_test_split on sklearn. This is the simplest way
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size = 0.2, random_state=42)

# However, need to use stratified sampling in order for the datasets to represent 
# the whole population. Let's say we want to stratify it by median income range

housing["income_cat"] = pd.cut(housing["median_income"],
                                bins=[0.,1.5,3.0,4.5,6., np.inf],
                                labels=[1,2,3,4,5]) #pd.cut creates categories by the labels
# housing["income_cat"].hist()
# plt.show()
# print(housing.head())

# Now we can perform stratified sampling
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# checking the proportion of the income category
print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))

# Now remove the income_cat feature so the data is back to its original state:
for set_ in (strat_test_set, strat_train_set):
    set_.drop("income_cat", axis = 1, inplace = True)