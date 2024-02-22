from models import Models
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = Models(X, y)

rfc_clf = model.rfc_clf()
ada_clf = model.ada_clf()
hgb_clf = model.hgb_clf()
gau_nb = model.gau_nb()
lgr = model.lgr()

print(rfc_clf)
print(ada_clf)
print(hgb_clf)
print(gau_nb)
print(lgr)