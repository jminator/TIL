import Ch3_1_simple_classification as sc
import numpy as np

## Measuring 'accuracy' using cross-validation ##

# The code below performes roughly the same thing as Scikit-learn's cross_val_score()
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone

skfolds = StratifiedKFold(n_splits=3, random_state=42)

for train_index, test_index in skfolds.split(sc.X_train, sc.y_train_5):
    clone_clf = clone(sc.sgd_clf)
    X_train_folds = sc.X_train[train_index]
    y_train_folds = sc.y_train_5[train_index]
    X_test_fold = sc.X_train[test_index]
    y_test_fold = sc.y_train_5[test_index]

    clone_clf.fit(X_train_folds, y_train_folds)
    y_pred = clone_clf.predict(X_test_fold)
    n_correct = sum(y_pred == y_test_fold)
    # print(n_correct / len(y_pred))

# StratifiedKFold performs stratified sampling.
# At each iteration the code creates a clone of the classifier, trains that clone on the training folds, and makes predictions on the test fold.
# Then it counts the number of correct predictions and outputs the ratio of correct predictions.

# If we use cross_val_score:
from sklearn.model_selection import cross_val_score
print(cross_val_score(sc.sgd_clf, sc.X_train, sc.y_train_5, cv = 3, scoring = "accuracy"))
# The output gives over 93% accuracy. However, this may not be the true accuracy

# Let's have look at a classifier that classifies every image as 'not-5':
from sklearn.base import BaseEstimator
class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)
never_5_clf = Never5Classifier()
cross_val_score(never_5_clf, sc.X_train, sc.y_train_5, cv = 3, scoring= "accuracy")
# This classifier gives over 90% accuracy
# This is because only about 10% of the images are 5s. 
# This is a 'skewed dataset' where some classes are much more frequent than others and accuracy test is not preferable for this type of datasets.


## Confusion matrix ##
# The idea is to count the number of times intances of class A are classified as class B
# To begin with, we need a set of predictions. Instead of using the test set, let's use cross_val_predict()
from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sc.sgd_clf, sc.X_train, sc.y_train_5, cv=3)
# This returns the predictions made on each test fold.

from sklearn.metrics import confusion_matrix
# print(confusion_matrix(sc.y_train_5, y_train_pred))
# The row represents an actual class, column represents a predicted class.
# The 1st row: 53,892 of them were correctly classified(true negative) as non-5s while remaining 687 were wrongly classified as 5s (false positive)
# the 2nd row: 1891 were wrongly classified as non-5s(false negative) while 3530 were correctly classified as 5s(true positive)

# precision of the classifier = TP / (TP+FP)
# recall(sensitivity or true positive rate) = TP / (TP+FN) = ratio of actually positive instances that are correctly detected by the classifier (실제 true중에서 모델이 true라고 예측한 비율)
from sklearn.metrics import precision_score, recall_score
# print(precision_score(sc.y_train_5, y_train_pred)) # gives about 0.73
# print(recall_score(sc.y_train_5, y_train_pred)) # gives about 0.75

# F1 score is a harmonic mean of precision and recall, which gives much more weight to low values.
# As a result, F1 score is high if both precision and recall are high
# F1 = 2 / [(1/precision) + (1/recall)] = 2 * [(precision * recall) / (precision + recall)] = TP / [ TP + (FN + FP)/2 ]
from sklearn.metrics import f1_score
# print(f1_score(sc.y_train_5, y_train_pred)) # gives about 0.74

# However, we cannot have both of them very high. Increasing precision reduces recall and vice versa.
# This is called the precision/recall trade-off
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
y_scores = cross_val_predict(sc.sgd_clf, sc.X_train, sc.y_train_5, cv = 5, method = "decision_function")
precisions, recalls, thresholds = precision_recall_curve(sc.y_train_5, y_scores)
def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="precision")
    plt.plot(thresholds, recalls[:-1], "g-", label = "recall")

# plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
# plt.show()

# To create 90% precision, 
threshold_90_precision = thresholds[np.argmax(precisions >= 0.90)]
# to make predictions instead of calling the classifier's predict() method,
y_train_pred_90 = (y_scores >= threshold_90_precision)
# to check,
precision_score(sc.y_train_5, y_train_pred_90)
recall_score(sc.y_train_5, y_train_pred_90)