# -------------------- Data Preprocessing in Python --------------------


# %%
# -------------------- Importing the Libraries --------------------
import pandas as pd
import numpy as np


# %%
# -------------------- Importing the Dataset --------------------
data = pd.read_csv('Dataset/Data.csv')

dataset.isna()
dataset.isna().sum()

# Separating feature values from the dependent variable
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


# %%
# -------------------- Taking Care of Missing Data --------------------
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


# %%
# -------------------- Encoding Categorical Data --------------------

# Encoding the independent variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# Exemples
# categorical_features = ['Sex', 'Embarked', 'Pclass']
# ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_features)], remainder='passthrough')

X = np.array(ct.fit_transform(X))

# %%
# Encoding the dependent variable
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)


# %%
# ---------- Splitting the Dataset Into the Training and Test Set ----------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# %%
# -------------------- Feature Scaling --------------------
# Not used in most ML models
'''
Standardization (always works)
Normalization (Works more for data that follows a standard deviation)
'''

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
