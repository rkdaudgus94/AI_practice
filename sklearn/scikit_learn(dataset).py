# 당뇨벙(diabetes) 환자들의 데이터 추출

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model 
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes()
regr = linear_model.LinearRegression()
print('shape of idabetes.data: ', diabetes.data.shape)
print(diabetes.data)

print('입력데이터의 특성들')
print(diabetes.feature_names) 

X = diabetes.data[:,np.newaxis, 2]
print(X)

regr.fit(X, diabetes.target)
print(regr.coef_,regr.intercept_)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data[:, np.newaxis,2], diabetes.target, test_size = 0.2)

regr = LinearRegression()
regr.fit(X_train, y_train)

score = regr.score(X_train, y_train)
print(score)
score = regr.score(X_test, y_test)
print(score)
