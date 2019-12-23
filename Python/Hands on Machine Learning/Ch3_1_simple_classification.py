from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1) # loads mnist dataset
# mnist.keys() 
# DESCR: key describing the dataset
# data: key containing an array with one row per instance and one column per feature
# target: key containing an array with the labels

X, y = mnist["data"], mnist["target"]
# print(X.shape) # there are 70,000 images and each image has 784 features(28x28 pixels)
# each pixel represents one pixel's intensity from 0 to 255

import matplotlib.pyplot as plt
some_digit = X[0]
# some_digit_image = some_digit.reshape(28, 28)

# plt.imshow(some_digit_image, cmap="binary")
# plt.axis("off")
# plt.show() # it shows '5'
# print(y[0])

# since the label is a string, convert it to numbers

import numpy as np
y = y.astype(np.uint8) # it's 'uint' not 'unit'

# creating training set and test set
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

## TRAINING A BINARY CLASSIFIER
# Let's say we are training a model that can classify number '5' or 'not 5'
y_train_5 = (y_train == 5) # returns 'true' for all 5s.
y_test_5 = (y_test == 5)

# Let's pick a classifier and train it. Let's go with Stochastic Gradient Descent(SGD) classifier.
# SGD is capable of handling very large datasets efficiently.
from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42) 
# since SGD relies on randomness during training, to have a reproducible results, should set random_state
sgd_clf.fit(X_train, y_train_5)
output = sgd_clf.predict([some_digit]) # predict if it is '5'
print(output) # gives 'true'
