import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

def svm(X_test):
        X_train = pd.read_csv("X_train.txt", sep=" ", header=None)
        y_train = pd.read_csv("y_train.txt", header=None)

                # Radial Basis Function kernal
        model = SVC(kernel='rbf', gamma=0.001, C=100)

        model.fit(X_train, y_train)# Make prediction
        y_pred = model.predict(X_test)# Evaluate our model
        return y_pred
