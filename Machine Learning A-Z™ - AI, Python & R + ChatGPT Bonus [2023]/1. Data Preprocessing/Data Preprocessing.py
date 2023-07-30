#################### Data Preprocessing ####################


# %%
#################### Importing the libraries ####################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
#################### Importing the dataset ####################

data = pd.read_csv('Dataset/Data.csv')

# Separating feature values from the dependent variable
features = data.iloc[:, :-1].values
dependent = data.iloc[:, -1].values


# %%
#################### Taking care of missing data ####################

