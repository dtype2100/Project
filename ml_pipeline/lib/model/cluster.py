import ray
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, SpectralClustering
from sklearn.cluster import AgglomerativeClustering, DBSCAN, HDBSCAN, OPTICS, Birch
from sklearn.metrics import silhouette_score


models_cluster = ['KMeans', 
    'AffinityPropagation', 
    'MeanShift', 
    'SpectralClustering'
    'AgglomerativeClustering', 
    'DBSCAN', 
    'HDBSCAN', 
    'OPTICS',
    'Birch'] 

@ray.remote
def cluster_models(model_name, X):
    result = {} # []
    if model_name == 'KMeans':
        model = KMeans(n_clusters=5, n_init="auto").fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'AffinityPropagation':
        model = AffinityPropagation().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'MeanShift':
        model = MeanShift().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'SpectralClustering':
        model = SpectralClustering().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'AgglomerativeClustering':
        model = AgglomerativeClustering().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'DBSCAN':
        model = DBSCAN().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'HDBSCAN':
        model = HDBSCAN().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    if model_name == 'OPTICS':
        model = OPTICS().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)
    
    if model_name == 'Birch':
        model = Birch().fit(X)
        result.update({'model': model_name, 'silhouette': silhouette_score(X, model.labels_)})
        # score = silhouette_score(X, model.labels_)

    return {'result':result} # {'model': model_name, 'score':score}
    
# @ray.remote
# def cluster_model2(X):
#     models = {'KMeans': KMeans(), 
#         'AffinityPropagation': AffinityPropagation(), 
#         'MeanShift': MeanShift(), 
#         'SpectralClustering': SpectralClustering(),
#         'AgglomerativeClustering': AgglomerativeClustering(), 
#         'DBSCAN': DBSCAN(), 
#         'HDBSCAN': HDBSCAN(), 
#         'OPTICS': OPTICS(),
#         'Birch': Birch()}
#     for model_name, model in models.items():
#         model.fit(X)
#         scores = silhouette_score(X, model.labels_)
#         print(model_name, scores)