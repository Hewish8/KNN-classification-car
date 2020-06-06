# -*- coding: utf-8 -*-
"""KNN Classification Cars.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YAQSJ6zs9Mz7AnvviVyZzZx5leVHPHFF
"""

pip install -U scikit-learn

#Predicting whether automatic or manual car
import numpy as np
import pandas as pd

import scipy
import matplotlib.pyplot as plt
from pylab import rcParams
import urllib
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from sklearn import metrics

#Upload the csv file
from google.colab import files
file = files.upload()

#Read the csv file
cars = pd.read_csv("mtcars.csv")
cars.head(30) #prints first 3 data

cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs', 'am','gear','card']
cars_input_columns= ['mpg', 'disp','hp', 'qsec']
#Choosing columns
X_prime = cars[cars_input_columns]
Y = cars[['am']]

#Do scaling of data
X =preprocessing.scale(X_prime)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= .33, random_state = 30) #.33 means 33% goes into test set, random is seed for reproducibility

# Training the data and build model
# Initiate KNN
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, Y_train)
print(clf)

Y_expect = Y_test
Y_pred = clf.predict(X_test)
#Use scikit learn mtrics module classification report function to analyse
print(metrics.classification_report(Y_expect, Y_pred))

#Testing randon inputs
data = np.array([30.4, 95.1, 113, 16.9]) # 1 x 4 array
P_data = preprocessing.scale(data)
#print(P_data)
Y_predict = clf.predict([P_data])
#print(Y_predict)

if Y_predict==0:
  print("Automatic Car")
else:
  print("Manual car")