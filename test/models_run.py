# mlflow server --host 127.0.0.1 --port 5000

import mlflow
from models import Classification, Regression,Cluster
from sklearn.datasets import load_iris

mlflow_uri = "http://127.0.0.1:5000"

X, y = load_iris(return_X_y=True)

clf = Classification(X, y, mlflow_uri)
clu = Cluster(X, y, mlflow_uri)
reg = Regression(X, y, mlflow_uri)

# classification mdoels
rfc_clf = clf.rfc_clf()
ada_clf = clf.ada_clf()
hgb_clf = clf.hgb_clf()
gau_nb = clf.gau_nb()
lgr = clf.lgr()

# Regression models
rfc_reg = reg.rfc_reg()
ada_reg = reg.ada_reg()
grad_reeg = reg.grad_reg()

# cluster mdoels
km = clu.kmeans()
db = clu.dbscan()

# clf models results
print(f'rfc_clf: {rfc_clf}')
print(f'ada_clf: {ada_clf}')
print(f'hgb_clf: {hgb_clf}')
print(f'gau_nb: {gau_nb}')
print(f'lgr: {lgr}')

# reg models results
print(f"rfc_reg: {rfc_reg}")
print(f"ada_reg: {ada_reg}")
print(f"grad_reg: {grad_reeg}")

# cluster models results
print(f'km: {km}')
print(f'db: {db}')
