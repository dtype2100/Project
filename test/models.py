import mlflow, uuid
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.cluster import KMeans, DBSCAN
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import silhouette_score, mean_absolute_error, r2_score


class Classification:
    
    def __init__(self, X, y, tracking_uri):
        self.X = X
        self.y = y
        mlflow.set_tracking_uri(tracking_uri)

    def __str__(self) -> str:
        return f"self.X: {self.X}, \n\n self.y: {self.y}"

    def rfc_clf(self):
        mlflow.set_experiment("RandomForestClassifier")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"RandomForestClassifier-{run_name}"):
            clf = RandomForestClassifier()
            score = cross_val_score(clf, self.X, self.y, cv=5).mean()
            mlflow.log_metric("accuracy", score)
            return score

    def ada_clf(self):
        mlflow.set_experiment("AdaBoostClassifier")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"AdaBoostClassifier-{run_name}"):
            clf = AdaBoostClassifier(algorithm='SAMME')
            score = cross_val_score(clf, self.X, self.y, cv=5).mean()
            mlflow.log_metric("accuracy", score)
            return score

    def hgb_clf(self):
        mlflow.set_experiment("GradientBoostingClassifier")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"GradientBoostingClassifier-{run_name}"):
            clf = GradientBoostingClassifier()
            score = cross_val_score(clf, self.X, self.y, cv=5).mean()
            mlflow.log_metric("accracy", score)
            return score

    def gau_nb(self):
        mlflow.set_experiment("GaussianNB")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"GaussianNB-{run_name}"):
            clf = GaussianNB()
            score = cross_val_score(clf, self.X, self.y, cv=5).mean()
            mlflow.log_metric("accracy", score)
            return score

    def lgr(self):
        mlflow.set_experiment("LogisticRegression")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"LogisticRegression-{run_name}"):
            clf = LogisticRegression(max_iter=1000)
            score = cross_val_score(clf, self.X, self.y, cv=5).mean()
            mlflow.log_metric("accracy", score)
            return score

class Regression:
    def __init__(self, X, y, tracking_uri):
        self.X = X
        self.y = y
        mlflow.set_tracking_uri(tracking_uri)

    def rfc_reg(self):
        mlflow.set_experiment("RandomForestRegressor")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"RandomForestRegressor-{run_name}"):
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=123, test_size=0.2)
            reg = RandomForestRegressor().fit(X_train, y_train)
            y_pred = reg.predict(X_test)
            mse = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            mlflow.log_metrics({"mse":mse, "r2": r2})
            return f"mse: {mse}, r2: {r2}"
    
    def ada_reg(self):
        mlflow.set_experiment("AdaBoostRegressor")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"AdaBoostRegressor-{run_name}"):
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=123, test_size=0.2)
            reg = AdaBoostRegressor().fit(X_train, y_train)
            y_pred = reg.predict(X_test)
            mse = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            mlflow.log_metrics({"mse":mse, "r2": r2})
            return f"mse: {mse}, r2: {r2}"
        
    def grad_reg(self):
        mlflow.set_experiment("GradientBoostingRegressor")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"GradientBoostingRegressor-{run_name}"):
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=123, test_size=0.2)
            reg = GradientBoostingRegressor().fit(X_train, y_train)
            y_pred = reg.predict(X_test)
            mse = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            mlflow.log_metrics({"mse":mse, "r2": r2})
            return f"mse: {mse}, r2: {r2}"

class Cluster:
    def __init__(self, X, y, tracking_uri):
        self.X = X
        self.y = y
        mlflow.set_tracking_uri(tracking_uri)
    
    def kmeans(self):
        mlflow.set_experiment("KMeans")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"KMeans-{run_name}"):
            clu = KMeans()
            score = silhouette_score(self.X, clu.fit_predict(self.X))
            mlflow.log_metric("silhouette", score)
            return score 
    
    def dbscan(self):
        mlflow.set_experiment("DBSCAN")
        run_name = str(uuid.uuid4())[:8]
        with mlflow.start_run(run_name=f"DBSCAN-{run_name}"):
            clu = DBSCAN()
            score = silhouette_score(self.X, clu.fit_predict(self.X))
            mlflow.log_metric("silhoutte", score)
            return score

