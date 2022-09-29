import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model 

regr = linear_model.LinearRegression()

X = [[164], [179], [162], [170]] # 선형회귀의 입력 (2차원)
y = [53, 63, 55, 59]
regr.fit(X, y)

plt.scatter(X, y, color='black')

y_pred = regr.predict(X)

plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()