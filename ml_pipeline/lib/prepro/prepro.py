import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def define_extention(data_file_path):
    file_extension = os.path.splitext(data_file_path)[1] # 파일 확장자 확인
    data_type = ''
    if file_extension == '.csv':
        data_type = 'Structured Data'
    elif file_extension in ['.txt', '.json', '.xml']:
        data_type = 'Text Data'
    elif file_extension in ['.jpg', '.png', '.gif']:
        data_type = 'Image Data'
    elif file_extension in ['.mp4', '.avi', '.mov']:
        data_type = 'Video Data'
    else:
        data_type = 'Unknown Data Type'
    return data_type

def data_prepro(categorical_features, data):
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
        # categorical_features = np.ravel(categorical_features) # select_dtypes를 출력하면 DataFrame로 나오기 때문에, np.ravel을 사용하여 np.array 형태로 변환 
        scaler = StandardScaler()
        numeric_features = scaler.fit_transform(numeric_features)

        datetime_columns = categorical_features.select_dtypes('datetime64')
        categorical_features = categorical_features.drop(columns=datetime_columns.columns) # datetime64 컬럼을 삭제
        # final_df = pd.concat([pd.DataFrame(numeric_features), pd.DataFrame(categorical_features)], axis=1)
        # print(final_df)
        # print(categorical_features)
        # print(numeric_features)
        return numeric_features, categorical_features #  {"numeric_features": numeric_features, "categorical_features": categorical_features}