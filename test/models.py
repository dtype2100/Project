from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, HistGradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score


class Models:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def rfc_clf(self):
        clf = RandomForestClassifier()
        score = cross_val_score(clf, self.X, self.y, cv=5).mean()
        return score

    def ada_clf(self):
        clf = AdaBoostClassifier(algorithm='SAMME')
        score = cross_val_score(clf, self.X, self.y, cv=5).mean()
        return score

    def hgb_clf(self):
        clf = HistGradientBoostingClassifier()
        score = cross_val_score(clf, self.X, self.y, cv=5).mean()
        return score

    def gau_nb(self):
        clf = GaussianNB()
        score = cross_val_score(clf, self.X, self.y, cv=5).mean()
        return score

    def lgr(self):
        clf = LogisticRegression(max_iter=1000)
        score = cross_val_score(clf, self.X, self.y, cv=5).mean()
        return score