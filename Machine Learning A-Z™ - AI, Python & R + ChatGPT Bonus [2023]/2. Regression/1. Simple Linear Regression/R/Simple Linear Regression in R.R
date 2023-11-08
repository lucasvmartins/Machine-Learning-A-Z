setwd("~/GitHub/Machine-Learning-A-Z/Machine Learning A-Z™ - AI, Python & R + ChatGPT Bonus [2023]/2. Regression/1. Simple Linear Regression/R")

# -------------------- Simple Linear Regression in R  --------------------

# ---------- Importing the Dataset ----------
data = read.csv('../Dataset/Salary_Data.csv')


# ---------- Splitting the dataset into the Training and Test set ----------
library(caTools)

set.seed(123)

split = sample.split(data$Salary, SplitRatio = 2/3)
training_set = subset(data, split == TRUE)
test_set = subset(data, split == FALSE)
