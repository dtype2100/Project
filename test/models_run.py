from models import Classification, Cluster
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

clf = Classification(X, y)
clu = Cluster(X, y)

# classification mdoels
rfc_clf = clf.rfc_clf()
ada_clf = clf.ada_clf()
hgb_clf = clf.hgb_clf()
gau_nb = clf.gau_nb()
lgr = clf.lgr()

print(f'rfc_clf: {rfc_clf}')
print(f'ada_clf: {ada_clf}')
print(f'hgb_clf: {hgb_clf}')
print(f'gau_nb: {gau_nb}')
print(f'lgr: {lgr}')

# cluster mdoels
km = clu.kmeans()
db = clu.dbscan()

print(f'km: {km}')
print(f'db: {db}')
