import ray
from lib.model.regression import reg_models

def fit_regressor(numeric_features, categorical_features, target_label):
    # 분류
    # if not ray.is_initialized():
    #     ray.init()
    models_reg = ['LinearRegression', 'Ridge Regression', 'Lasso Regression', 'Elastic Net', 'SVR', 'KNeighborsRegressor'] # 'Polynomial Regression'
    ray_reg_tasks = [reg_models.remote(model_name, numeric_features, categorical_features[target_label]) for model_name in models_reg]
    ray_reg_result = ray.get(ray_reg_tasks)
    for n in range(len(models_reg)):
        print(f"model: {ray_reg_result[n]['model']}, mse: {ray_reg_result[n]['mse']}, r2: {ray_reg_result[n]['r2']}")
    # ray.shutdown()