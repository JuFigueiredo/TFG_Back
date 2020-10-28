import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

X_train = pd.read_csv("X_train2.txt", sep=" ", header=None)
y_train = pd.read_csv("y_train2.txt", header=None)
X_test = pd.read_csv("X_test2.txt", sep=" ", header=None)
y_test = pd.read_csv("y_test2.txt", header=None)

rna = MLPClassifier(activation = 'tanh', alpha = 0.001, batch_size = 10, learning_rate = 'constant', solver = 'sgd')

rna.fit(X_train, y_train)  # Make prediction
y_pred = rna.predict(X_test)

print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))
print(metrics.accuracy_score(y_test, y_pred))