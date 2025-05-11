#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 11 10:47:37 2025

@author: almohanadalfarei
"""





import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([1, 4, 6, 7, 8]).reshape((-1, 1)) 
y = np.array([20,30,40,50,60]) 
model = LinearRegression()
model.fit(x, y)

print(model.fit(x, y))

r_sq = model.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)


y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

plt.scatter(x, y, color='red', label='Actual Data')
plt.plot(x, y_pred, color='green', label='Regression Line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.legend()
plt.show()






























