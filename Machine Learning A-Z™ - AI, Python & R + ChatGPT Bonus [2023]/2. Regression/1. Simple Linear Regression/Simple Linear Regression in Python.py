# -------------------- Simple Linear Regression in Python  --------------------

#%%
# -------------------- Importing the Libraries --------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#%%
# -------------------- Importing the Dataset --------------------
data = pd.read_csv('Dataset/Salary_Data.csv')

# Check for missing values

# Separating feature values from the dependent variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]


#%%
# ---------- Splitting the Dataset Into the Training and Test Set ----------
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#%%
# -------------------- Importing the Dataset --------------------
regressor = 

