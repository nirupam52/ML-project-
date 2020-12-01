from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def pre_coeffs():
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.30, random_state=69)

    reg_model = linear_model.LinearRegression()
    reg_model.fit(X_train, y_train)

    return reg_model.coef_

