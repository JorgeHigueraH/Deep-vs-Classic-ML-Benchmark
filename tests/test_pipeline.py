import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocessing import DataPreprocessor

def run_test():
    df = pd.read_csv('data/csv/users_data.csv')
    
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.preprocess_data(df)
    
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)
    
    print("\nColumnas finales en X_train:")
    print(X_train.columns.tolist())
    
    print("\nMuestra de datos transformados (primeras 3 filas):")
    print(X_train.head(3))

if __name__ == "__main__":
    run_test()