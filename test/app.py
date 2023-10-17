from prepro_lib import define_extention, label_encoder, onehot_encoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

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
    label_num = len(y.unique())

    numeric_features = data.select_dtypes(include=['float64', 'int64'])
    categorical_features = data.select_dtypes(include=['object']) 
    # categorical_features = np.ravel(categorical_features) # select_dtypes를 출력하면 DataFrame로 나오기 때문에, np.ravel을 사용하여 np.array 형태로 변환 
    
    scaler = StandardScaler()
    numeric_features = scaler.fit_transform(numeric_features)

    for col in categorical_features.columns:
        if categorical_features[col].str.match(r'\d{4}-\d{2}-\d{2}').all() == True or categorical_features[col].str.match(r'\d{4}:\d{2}:\d{2}').all() == True:
            categorical_features[col] = pd.to_datetime(categorical_features[col])
            categorical_features['year'] = categorical_features[col].dt.year
            categorical_features['month'] = categorical_features[col].dt.month
            categorical_features['day'] = categorical_features[col].dt.day
            categorical_features['hour'] = categorical_features[col].dt.hour
            categorical_features['minute'] = categorical_features[col].dt.minute
        else:
            encoder = LabelEncoder()
            categorical_features[col] = encoder.fit_transform(categorical_features[col])
    
    datetime_columns = categorical_features.select_dtypes('datetime64')
    # datetime64 컬럼을 삭제
    categorical_features = categorical_features.drop(columns=datetime_columns.columns)
    # final_df = pd.concat([pd.DataFrame(numeric_features), pd.DataFrame(categorical_features)], axis=1)
    # print(final_df)
    print(categorical_features)
    X_train, X_test, y_train, y_test = train_test_split(numeric_features, categorical_features, test_size=0.3, shuffle=True, random_state=42)


# 분류, 회귀, 시계열, 이상탐지

# Result: Rank, Model, Score

# pkl, onnx 생성