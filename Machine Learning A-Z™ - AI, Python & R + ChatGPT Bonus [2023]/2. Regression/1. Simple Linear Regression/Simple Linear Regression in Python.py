# -------------------- Simple Linear Regression in Python  --------------------

#%%
# -------------------- Importing the Libraries --------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%%
# -------------------- Importing the Dataset --------------------
data = pd.read_csv('Dataset/Salary_Data.csv')

# Check for missing values

# Separating feature values from the dependent variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]


#%%
# ---------- Splitting the Dataset Into the Training and Test Set ----------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#%%
# -------------------- Training the Model --------------------
from sklearn.linear_model import LinearRegression
regressor = LinearRegression() # Creating the object of the model

regressor.fit(X_train, y_train) # Fitting the model with de training sets


#%%
# -------------------- Predicting the Test Sets --------------------
regressor.predict(X_test)
