import ray
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope, MinCovDet
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(y_true, y_pred, model_name):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=1)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=1)
    f1 = f1_score(y_true, y_pred, average='weighted')
    # print(f"model: {model_name}, accuracy: {accuracy}, precision: {precision}, recall: {recall}, f1-score: {f1}")
    return {"model": model_name, "accuracy": accuracy, "precision": precision, "recall": recall, "f1-score": f1}

@ray.remote
def anomaly_models(model_name, X, y):
    result = []
    if model_name == 'EllipticEnvelope':
        model = EllipticEnvelope().fit(X)
        # scores = model.decision_function(X)  
        pred = model.predict(X)
        result.append(evaluate_model(y, pred, model_name))

    if model_name == 'IsolationForest':
        model = IsolationForest().fit(X)
        # scores = model.decision_function(X)  
        pred = model.predict(X)
        result.append(evaluate_model(y, pred, model_name))
    
    if model_name == 'LocalOutlierFactor':
        model = LocalOutlierFactor().fit(X) # novelty=True, .decision_function(X) 
        # scores = model.negative_outlier_factor_  
        pred = model.fit_predict(X)
        result.append(evaluate_model(y, pred, model_name))

    if model_name == 'OneClassSVM':
        model = OneClassSVM().fit(X)
        # scores = model.decision_function(X) 
        pred = model.predict(X)
        result.append(evaluate_model(y, pred, model_name))

    # if model_name == 'MinCovDet':
    #     model = MinCovDet().fit(X)
    #     pred = model.mahalanobis(X)  
    #     percentile = 75
    #     threshold = np.percentile(y_mcd_pred, percentile) # 이상치로 판단할 임계값 설정
    #     y_mcd_pred = (pred > threshold).astype(int) # Mahalanobis 거리가 임계값보다 큰 경우 이상치로 분류
    #     evaluate_model(y, y_mcd_pred, "MinCovDet")

    # if model_name == 'NearestNeighbors':
    #     model = NearestNeighbors().fit(X)
    #     neighbors = model.kneighbors(X)

    # if model_name == 'PCA':
    #     model = PCA().fit(X)
        # scores = None  
    
    return result # {"model": model_name, "scores": scores}
