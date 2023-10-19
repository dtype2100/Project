import ray
import mlflow
import mlflow.pyfunc
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# 분류 모델
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
# from xgboost import XGBClassifier

@ray.remote
def clf_models(model_name, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    if model_name == 'LogisticRegression':
        model = LogisticRegression()
    if model_name == 'SVC':
        model = SVC()
    if model_name == 'GaussianNB':
        model = GaussianNB()
    if model_name == 'DecisionTreeClassifier':
        model = DecisionTreeClassifier()
    if model_name == 'RandomForestClassifier':
        model = RandomForestClassifier()
    if model_name == 'KNeighborsClassifier':
        model = KNeighborsClassifier()
    if model_name == 'MLPClassifier':
        model = MLPClassifier()
    if model_name == 'AdaBoostClassifier':
        model = AdaBoostClassifier()
    if model_name == 'GradientBoostingClassifier':
        model = GradientBoostingClassifier()
    # if model_name == 'XGBoost':
    #     model = XGBClassifier()

    # 모델 훈련
    model.fit(X_train, y_train)
    
    # 테스트 데이터로 예측
    y_pred = model.predict(X_test)
    
    # 정확도 계산
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # MLflow로 결과를 추적
    # with mlflow.start_run():
    #     mlflow.log_metric('accuracy', accuracy)
    #     mlflow.log_metric('precision', precision)
    #     mlflow.log_metric('recall', recall)
    #     mlflow.log_metric('f1_score', f1_score)
    #     mlflow.set_tag('model', model_name)

    return  {"model": model_name, "y_pred": y_pred, "accuracy": accuracy,
             "precision": precision, "recall": recall, "f1_score": f1}

