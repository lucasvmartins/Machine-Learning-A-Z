#################### Data Preprocessing ####################


# %%
#################### Importing The Libraries ####################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
#################### Importing The Dataset ####################

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
