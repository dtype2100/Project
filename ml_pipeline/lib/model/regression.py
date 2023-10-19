import ray
import mlflow
import mlflow.pyfunc

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# 회귀 모델
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

# @ray.remote
# def reg_models(model_name, X, y):

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     if model_name == 'Linear Regression':
#         model = LinearRegression()
#         # y_pred = model.predict(X_test)
#     elif model_name == 'Ridge Regression':
#         model = Ridge(alpha=1.0)  # alpha는 규제 강도를 조절.
#         # y_pred = model.predict(X_test)
#     elif model_name == 'Lasso Regression':
#         model = Lasso(alpha=1.0)  
#         # y_pred = model.predict(X_test)
#     elif model_name == 'Elastic Net':
#         model = ElasticNet(alpha=1.0, l1_ratio=0.5)  # alpha와 l1_ratio를 조절.
#         # y_pred = model.predict(X_test)
#     # elif model_name == 'Polynomial Regression':
#     #     poly = PolynomialFeatures(degree=2)
#     #     X_test_poly = poly.transform(X_test)
#     #     y_pred = model.predict(X_test_poly)
#     elif model_name == 'SVR':
#         model = SVR(kernel='linear', C=1.0)  # kernel과 C를 조절.
#         # y_pred = model.predict(X_test)
#     elif model_name == 'K-Nearest Neighbors Regression':
#         model = KNeighborsRegressor(n_neighbors=5)  # 이웃의 수를 조절.
#         # y_pred = model.predict(X_test)
#     y_pred = model.predict(X_test)

#     model.fit(X_train, y_train)
#     mse = mean_squared_error(y_test, y_pred)
#     r2 = r2_score(y_test, y_pred)
    
#     # MLflow로 결과를 추적
#     # with mlflow.start_run():
#     #     mlflow.log_metric('accuracy', mse)
#     #     mlflow.log_metric('accuracy', r2)
#     #     mlflow.set_tag('model', model_name)

#     return  {"model": model_name, "y_pred": y_pred, "mse": mse, "r2": r2}

@ray.remote
def reg_models(model_name, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    if model_name == 'LinearRegression':
        model = LinearRegression()
    elif model_name == 'Ridge Regression':
        model = Ridge(alpha=1.0)
    elif model_name == 'Lasso Regression':
        model = Lasso(alpha=1.0)
    elif model_name == 'Elastic Net':
        model = ElasticNet(alpha=1.0, l1_ratio=0.5)
    elif model_name == 'SVR':
        model = SVR(kernel='linear', C=1.0)
    elif model_name == 'KNeighborsRegressor':
        model = KNeighborsRegressor(n_neighbors=5)
    else:
        raise ValueError(f"Unknown model_name: {model_name}")
    
    model.fit(X_train, y_train)  # 모델 훈련
    y_pred = model.predict(X_test)  # 모델 예측
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return  {"model": model_name, "y_pred": y_pred, "mse": mse, "r2": r2}
