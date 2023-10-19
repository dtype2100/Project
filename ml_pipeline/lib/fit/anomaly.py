import ray
from lib.model.anomaly import anomaly_models

def fit_anomaly(numeric_features, categorical_features, target_label):
    # if not ray.is_initialized():
    #     ray.init()
    models_anomaly = ['EllipticEnvelope', 'MinCovDet', 'IsolationForest', 'LocalOutlierFactor', 'OneClassSVM']
    ray_anomaly_tasks = [anomaly_models.remote(model_name.strip(), numeric_features, categorical_features[target_label]) for model_name in models_anomaly]
    ray_anomaly_result = ray.get(ray_anomaly_tasks)

    for result in ray_anomaly_result:
        print("result: ", result)
    # ray.shutdown()