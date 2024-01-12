import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle


def train_linear_regression(X_train, y_train, X_test, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    save_model(model, 'linear_regression_model.pkl')
    evaluate_model(model, X_test, y_test)


def train_random_forest(X_train, y_train, X_test, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    save_model(model, 'random_forest_model.pkl')
    evaluate_model(model, X_test, y_test)


def train_support_vector(X_train, y_train, X_test, y_test, target_column):
    if target_column == "CGPA in BS Fifth semester":
        file_name = 'cgpa'
    else:
        file_name = 'sgpa'
    model = SVR()
    model.fit(X_train, y_train)
    save_model(model, f'support_vector_model_{file_name}.pkl')
    evaluate_model(model, X_test, y_test)


def train_decision_tree(X_train, y_train, X_test, y_test):
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    save_model(model, 'decision_tree_model.pkl')
    evaluate_model(model, X_test, y_test)


def train_gradient_boosting(X_train, y_train, X_test, y_test, target_column):
    if target_column == "CGPA in BS Fifth semester":
        file_name = 'cgpa'
    else:
        file_name = 'sgpa'
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    save_model(model, f'gradient_boosting_model_{file_name}.pkl')
    evaluate_model(model, X_test, y_test)


def train_lasso_regression(X_train, y_train, X_test, y_test):
    model = Lasso(alpha=0.1)
    model.fit(X_train, y_train)
    save_model(model, 'lasso_regression_model.pkl')
    evaluate_model(model, X_test, y_test)


def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')


if __name__ == '__main__':
    df = pd.read_excel("Final Data Set 2.xlsx")

    df["Gender"] = df["Gender"].replace({"Male": 0, "Female": 1})
    df["Availing any scholarship"] = df["Availing any scholarship"].replace({"NO": 0, "YES": 1})

    mapping = {
        "Strongly disagree": 0,
        "Disagree": 1,
        "Neutral": 2,
        "Agree": 3,
        "Strongly Agree": 4
    }

    df["I opted for this program of study because of my own interest."] = df[
        "I opted for this program of study because of my own interest."].replace(mapping)
    for column in df.columns:
        column_average = df[column].mean(skipna=True)
        df[column].fillna(column_average, inplace=True)

    input_columns = ['Gender', 'Availing any scholarship', 'Matric percentage',
                     'Intermediate percentage', 'SGPA in BS First semester',
                     'SGPA in BS Second semester', 'SGPA in BS Third semester',
                     'SGPA in BS Fourth semester', 'I opted for this program of study because of my own interest.']
    target_columns = ['SGPA in BS Fifth semester', 'CGPA in BS Fifth semester']

    target_column_sgp5 = 'SGPA in BS Fifth semester'

    target_column_cgpa5 = 'CGPA in BS Fifth semester'

    X = df[input_columns]
    y = df[target_columns]

    # Split the data into training and testing sets
    X_train = df.loc[2:46, input_columns]
    y_train = df.loc[2:46, target_columns]

    X_test = df.loc[47:, input_columns]
    y_test = df.loc[47:, target_columns]

    train_linear_regression(X_train, y_train, X_test, y_test)
    train_random_forest(X_train, y_train, X_test, y_test)
    train_support_vector(X_train, y_train[target_column_sgp5], X_test, y_test[target_column_sgp5], target_column_sgp5)
    train_support_vector(X_train, y_train[target_column_cgpa5], X_test, y_test[target_column_cgpa5],
                         target_column_cgpa5)
    train_decision_tree(X_train, y_train, X_test, y_test)
    train_gradient_boosting(X_train, y_train[target_column_sgp5], X_test, y_test[target_column_sgp5], target_column_sgp5)
    train_gradient_boosting(X_train, y_train[target_column_sgp5], X_test, y_test[target_column_sgp5],
                            target_column_cgpa5)
    train_lasso_regression(X_train, y_train, X_test, y_test)
