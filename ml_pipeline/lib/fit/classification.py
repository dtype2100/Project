import ray
from lib.model.classification import clf_models

def fit_classification(numeric_features, categorical_features, target_label):
    # 분류
    # if not ray.is_initialized():
    #     ray.init()
    models_clf = ['LogisticRegression', 'SVC', 'GaussianNB', 'DecisionTreeClassifier', 'RandomForestClassifier', 'KNeighborsClassifier', 'MLPClassifier', 'AdaBoostClassifier', 'GradientBoostingClassifier'] # 'XGBoost'
    ray_clf_tasks = [clf_models.remote(model_name, numeric_features, categorical_features[target_label]) for model_name in models_clf]
    ray_clf_result = ray.get(ray_clf_tasks)
    for n in range(len(models_clf)):
        print(f"model: {ray_clf_result[n]['model']}, accuracy: {ray_clf_result[n]['accuracy']}, precision: {ray_clf_result[n]['precision']}, recall: {ray_clf_result[n]['recall']}, f1: {ray_clf_result[n]['f1_score']}")
    # ray.shutdown()