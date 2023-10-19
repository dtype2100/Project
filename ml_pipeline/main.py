import ray
from lib.prepro.prepro import define_extention, data_prepro
import pandas as pd
# import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder # , OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from lib.fit.anomaly import fit_anomaly
from lib.fit.classification import fit_classification
from lib.fit.cluster import fit_cluster
from lib.fit.regressor import fit_regressor

# 데이터 파일 경로 설정
# data_path = '../CNC_data_sum.csv'  
data_path = '../Test_01.csv'
data_type = define_extention(data_path) # Structured Data, Text Data, Image Data, Video Data, Unknown Data Type

if data_type == 'Structured Data':
    data = pd.read_csv(data_path)
# print(f'Data Type: {data_type}')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]
# 데이터 탐색 (만약 정형 데이터인 경우)
if data_type == 'Structured Data':
    data = pd.read_csv(data_path)
    label_num = len(y.unique())

    target_label = y.name # 타겟 데이터 column name 변수 할당
    categorical_features = data.select_dtypes(include=['object']) # DataFrame에서 모든 object type 데이터 선택

    if categorical_features.empty == True: # object type의 범주형 데이터가 없는 경우(int, float 데이터만 있는 경우)
        df_excluded = data.drop(columns=target_label)
        numeric_features = df_excluded.select_dtypes(include=['float64', 'int64', 'int32'])
        scaler = StandardScaler()
        numeric_features = scaler.fit_transform(numeric_features)

    # numeric_features = data.select_dtypes(include=['float64', 'int64'])
    # # categorical_features = np.ravel(categorical_features) # select_dtypes를 출력하면 DataFrame로 나오기 때문에, np.ravel을 사용하여 np.array 형태로 변환 
    # scaler = StandardScaler()
    # numeric_features = scaler.fit_transform(numeric_features)

    if categorical_features.empty == False: # 타겟 데이터가 object로 존재하는 경우
        for col in categorical_features.columns:
            # 시간 데이터가 object 타입인 경우, datetime로 변경 및 머신러닝에 학습할 수 있도록 분리
            if categorical_features[col].str.match(r'\d{4}-\d{2}-\d{2}').all() == True or categorical_features[col].str.match(r'\d{4}:\d{2}:\d{2}').all() == True:
                categorical_features[col] = pd.to_datetime(categorical_features[col])
                categorical_features['year'] = categorical_features[col].dt.year
                categorical_features['month'] = categorical_features[col].dt.month
                categorical_features['day'] = categorical_features[col].dt.day
                categorical_features['hour'] = categorical_features[col].dt.hour
                categorical_features['minute'] = categorical_features[col].dt.minute
            else: # 시간 데이터가 object로 존재하지 않는 경우, 정수 인코딩
                encoder = LabelEncoder()
                categorical_features[col] = encoder.fit_transform(categorical_features[col])
  
            numeric_features = data.select_dtypes(include=['float64', 'int64'])
            scaler = StandardScaler()
            numeric_features = scaler.fit_transform(numeric_features)

            datetime_columns = categorical_features.select_dtypes('datetime64')
            categorical_features = categorical_features.drop(columns=datetime_columns.columns) # datetime64 컬럼을 삭제

    # X_train, X_test, y_train, y_test = train_test_split(numeric_features, categorical_features, test_size=0.3, shuffle=True, random_state=42)
    
    if not ray.is_initialized():
        ray.init()
    clf = fit_classification(numeric_features, categorical_features, target_label)
    reg = fit_regressor(numeric_features, categorical_features, target_label)
    clu = fit_cluster(numeric_features)
    ano = fit_anomaly(numeric_features, categorical_features, target_label)
    # print(clf)
    # print(reg)
    # print(clu)
    # print(ano)
    ray.shutdown()