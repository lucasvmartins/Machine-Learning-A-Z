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


# ---------- Fitting Simple Linear Regression to the Training set ----------
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)


# ---------- Predicting the Test set Results ----------
y_pred = predict(regressor, newdata = test_set)


# ---------- Visualising the Training set Results ----------
# install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary per Years of Experience (Training set)') +
  xlab('Years of Experience') +
  ylab('Salary')


# ---------- Visualising the Test set Results ----------
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary per Years of Experience (Test set)') +
  xlab('Years of Experience') +
  ylab('Salary')

