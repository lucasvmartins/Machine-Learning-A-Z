# -------------------- Data Preprocessing in R --------------------

# -------------------- Importing the Libraries --------------------
data = read.csv('Dataset/Data.csv')
# data = data[2:3]


# -------------------- Taking Care of Missing Data --------------------
data$Age = as.integer(ifelse(is.na(data$Age),
                             ave(data$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                             data$Age))

data$Salary = (ifelse(is.na(data$Salary),
                      ave(data$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                      data$Salary))


# -------------------- Encoding Categorical Data --------------------
data$Country = factor(data$Country,
                      levels = c('France', 'Spain', 'Germany'),
                      labels = c(1, 2, 3))

data$Purchased = factor(data$Purchased,
                      levels = c('Yes', 'No'),
                      labels = c(1, 0))


# -------------------- Splitting The Dataset Into Training and Test Set --------------------
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(data$Purchased, SplitRatio = 0.8)
training_set = subset(data, split == TRUE)
test_set = subset(data, split == FALSE)


# -------------------- Feature Scaling --------------------
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])


