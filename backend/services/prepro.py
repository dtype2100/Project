import pandas as pd
from typing import Union, Dict, Any
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Preprocessing:
    def __init__(self):
        pass

    def prepro_all_columns(
            self, 
            df_data: Union[str, Dict[str, Any]], 
            payload: Dict[str, str]
            ) -> pd.DataFrame:
        
        df = pd.read_json(df_data)
        for _, var in payload.items():
            if var == 'all_col_dropna':
                df.dropna(inplace=True)

            elif var == 'all_col_bfill':
                df.fillna(method='bfill', inplace=True)

            elif var == 'all_col_ffill':
                df.fillna(method='ffill', inplace=True)

            elif var == 'minmax_scale':  
                scaler = MinMaxScaler()
                df = scaler.fit_transform(df)

            elif var == 'standard_scale':
                scaler = StandardScaler()
                df = scaler.fit_transform(df)

        return df
