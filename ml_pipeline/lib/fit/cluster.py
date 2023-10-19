import ray
from lib.model.cluster import cluster_models

def fit_cluster(numeric_features):
    # if not ray.is_initialized():
    #     ray.init()
    models_cluster = ['KMeans', 'AffinityPropagation', 'MeanShift', 'SpectralClustering','AgglomerativeClustering', 'DBSCAN', 'HDBSCAN', 'OPTICS', 'Birch'] 
    ray_cluster_tasks = [cluster_models.remote(model_name, numeric_features) for model_name in models_cluster]
    ray_cluster_result = ray.get(ray_cluster_tasks)
    for result in ray_cluster_result:
        print(f"{result['result']}")
    # ray.shutdown()