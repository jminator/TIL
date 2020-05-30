## MULTICLASS CLASSIFICATIONS ##
# Some algorithms like SGD, RF, naive Bayes classifiers are capable of handling multiple classes natively.
# Others like Logistic Regression, SVM are strictly binary.

# One-versus-One (OvO) strategy: train a binary classifier for every pair of digits. for example,
# one to distnguish 0s and 1s, another to distinguish 0s and 2s, and so on. So for N classes, total of 
# N * (N-1)/2 classifiers should be trained. The advantage of this strategy is that each classifier
# only needs to be trained on the part of the training set for the two classes that it must distinguish.
# For some algorithms like SVM, OvO is preferred because it is faster to train many classifiers on small
# training sets than to train few classifiers on large training sets.

# One-versus-the-Rest (OvR or OvA) strategy: train a binary classifier for each class. for example,
# one to detect 1, another to detect 2, and so on. Then when you want to classify an image, you get the
# decision score from each classifier for that image and select the class whose classifier outputs the 
# highest score. This strategy is preferred for most binary classification algorithms.

# Let's try with a SVM
from sklearn.svm import SVC
import Ch3_1_simple_classification as sc
X_train, y_train, some_digit = sc.X_train, sc.y_train, sc.some_digit

svm_clf = SVC()
svm_clf.fit(X_train, y_train)
print(svm_clf.predict([some_digit]))

# if you call the decision_function() method, it shows 10 scores per instance.
some_digit_scores = svm_clf.decision_function([some_digit])
print(some_digit_scores)

import numpy as np
np.argmax(some_digit_scores) # gives 5
svm_clf.classes_ # shows [0, 1, ... , 9]

# training SGDClassifier
from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42) 
sgd_clf.fit(X_train, y_train)
sgd_clf.predict([some_digit])

from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
cross_val_score(sgd_clf, X_train_scaled, y_train, cv=3, scoring="accuracy")




