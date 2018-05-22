# Import
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
# Load iris dataset
from sklearn.datasets import load_iris
from sklearn import metrics

from sklearn.grid_search import GridSearchCV

from datetime import datetime

# Instantiate
iris = load_iris()

# Create training and feature
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

dtc = DecisionTreeClassifier(random_state=0)

# # 2. Fit
# dtc.fit(X_train, y_train)

# # 3. Predict, there're 4 features in the iris dataset
# y_pred_class = dtc.predict(X_test)

# mas = metrics.accuracy_score(y_test, y_pred_class)
# print(mas,"\n")


# # Define the parameter values that should be searched
# sample_split_range = list(range(1, 50))

# Create a parameter grid: map the parameter names to the values that should be searched
# Simply a python dictionary
# Key: parameter name
# Value: list of values that should be searched for that parameter
# Single key-value pair for param_grid
# param_grid = dict(min_samples_split=sample_split_range)

now = datetime.now()
print (now)

param_grid = {
    "criterion": ['entropy', 'gini'],
    "splitter": ['best', 'random'],
    "presort": [False, True],
    "max_depth": list(range(1, 50)),
    "min_samples_split": list(range(2, 1000)),
    "min_samples_leaf": list(range(1, 1000))
}

# instantiate the grid
grid = GridSearchCV(dtc, param_grid, cv=10, scoring='accuracy')

# fit the grid with data
grid.fit(X_train, y_train)
# examine the best model

# Single best score achieved across all params (min_samples_split)
print(grid.best_score_)

# Dictionary containing the parameters (min_samples_split) used to generate that score
print(grid.best_params_)

# Actual model object fit with those best parameters
# Shows default parameters that we did not specify
print(grid.best_estimator_)
