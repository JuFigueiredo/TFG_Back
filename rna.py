import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

def rna(X_test):
    X_train = pd.read_csv("X_train.txt", sep=" ", header=None)
    y_train = pd.read_csv("y_train.txt", header=None)

    rna = MLPClassifier(activation = 'tanh', alpha = 0.001, batch_size = 10, learning_rate = 'constant', solver = 'sgd')

    rna.fit(X_train, y_train)  # Make prediction
    y_pred = rna.predict(X_test)

    return y_pred