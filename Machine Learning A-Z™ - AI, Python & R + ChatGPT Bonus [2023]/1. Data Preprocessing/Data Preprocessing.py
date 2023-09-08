#################### Data Preprocessing ####################


# %%
#################### Importing the Libraries ####################
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


# %%
#################### Importing the Dataset ####################
data = pd.read_csv('Dataset/Data.csv')

# Separating feature values from the dependent variable
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


# %%
#################### Taking Care of Missing Data ####################
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])


# %%
#################### Encoding Categorical Data ####################

# Encoding the independent variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')

x = np.array(ct.fit_transform(x))

# %%
# Encoding the dependent variable
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)


# %%
########## Splitting the Dataset Into the Training and Test Set ##########
from sklearn.model_selection import train_test_split

X_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


# %%
#################### Feature Scaling ####################
# Not used in most ML models
'''
Standardization (always works)
Normalization (Works more for data that follows a standard deviation)
'''

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])

