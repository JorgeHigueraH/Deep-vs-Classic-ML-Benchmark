import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def preprocess_data(self, df):
        X = df.drop('converted_to_pro', axis=1)
        X = X.drop('user_id', axis=1)
        y = df['converted_to_pro']
        
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        numeric_cols = X.select_dtypes(include=numerics).columns.tolist()
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        
        X_train = pd.get_dummies(X_train, drop_first=True)
        X_test = pd.get_dummies(X_test, drop_first=True)
        
        X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)
        
        X_train[numeric_cols] = self.scaler.fit_transform(X_train[numeric_cols])
        X_test[numeric_cols] = self.scaler.transform(X_test[numeric_cols])
        
        return X_train, X_test, y_train, y_test