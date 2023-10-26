# -------------------- Simple Linear Regression in Python  --------------------

#%%
# -------------------- Importing the Libraries --------------------
import pandas as pd
import numpy as np



#%%
# -------------------- Importing the Dataset --------------------
data = pd.read_csv('Dataset/Salary_Data.csv')

# Check for missing values

# Separating feature values from the dependent variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

#%%
# ---------- Splitting the Dataset Into the Training and Test Set ----------
