#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:32:04 2025

@author: almohanadalfarei
"""

import pandas as pd
#import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = pd.read_csv("/Users/almohanadalfarei/Downloads/heart.csv")

X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

full_model = LogisticRegression(penalty='none', solver='lbfgs', max_iter=1000)
full_model.fit(X_train_scaled, y_train)
full_preds = full_model.predict(X_test_scaled)
full_accuracy = accuracy_score(y_test, full_preds)
print(f" Full Model Accuracy: {full_accuracy*100:.2f}%")

lasso_model = LogisticRegression(penalty='l1', solver='liblinear', C=1.0, max_iter=1000)
lasso_model.fit(X_train_scaled, y_train)
lasso_preds = lasso_model.predict(X_test_scaled)
lasso_accuracy = accuracy_score(y_test, lasso_preds)
print(f" Lasso Model Accuracy: {lasso_accuracy*100:.2f}%")

coefficients = pd.Series(lasso_model.coef_[0], index=X.columns)
selected_vars = coefficients[coefficients != 0]
removed_vars = coefficients[coefficients == 0]

print("\nSelected Variables (non-zero coefficients):")
print(selected_vars)

print("\n Removed Variables (zero coefficients):")
print(removed_vars)

print("\n Summary:")
print(f"Variables selected: {len(selected_vars)}")
print(f"Variables removed: {len(removed_vars)}")
print(f"Accuracy improved? {'Yes' if lasso_accuracy > full_accuracy else 'No'}")
