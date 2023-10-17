# -------------------- Data Preprocessing in R --------------------

# -------------------- Importing the Libraries --------------------
data = read.csv('Dataset/Data.csv')


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

