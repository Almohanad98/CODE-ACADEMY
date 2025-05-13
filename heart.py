#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:32:04 2025

@author: almohanadalfarei
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np


data = pd.read_csv('/Users/almohanadalfarei/Downloads/heart.csv')
data

data.info()

no_d = data[data['target'] == 0]
yes_d = data[data['target'] == 1]
yes_d

X = data.drop('target',axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=121)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

LR_model = LogisticRegression()
LR_model.fit(x_train_scaled, y_train)
pred = LR_model.predict(x_test_scaled).reshape(-1, 1)
accuracy = accuracy_score(y_test, pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))


list1 = [86.3,84.4,83.9,83.9,80.5,84.9]
avg = np.mean(list1)
print("The Average score {:.2f}%".format(avg))