import pandas as pd
import numpy as np
import os

def generate_dataset(n_samples=100000):
    np.random.seed(42)
    
    data = {
        'user_id': range(n_samples),
        'days_since_signup': np.random.randint(1, 365, n_samples),
        'sessions_last_7_days': np.random.randint(0, 50, n_samples),
        'avg_session_duration': np.random.uniform(0.5, 30.0, n_samples),
        'budgets_created': np.random.randint(0, 100, n_samples),
        'pdfs_downloaded': np.random.randint(0, 40, n_samples),
        'clients_added': np.random.randint(0, 20, n_samples),
        'sector': np.random.choice(['construction', 'consulting', 'retail', 'education'], n_samples)
    }
    
    df = pd.DataFrame(data)
    
    noise = np.random.normal(0, 1, n_samples)
    score = (
        0.3 * df['budgets_created'] + 
        0.5 * df['pdfs_downloaded'] + 
        0.2 * df['sessions_last_7_days'] - 
        0.1 * df['days_since_signup'] + 
        noise
    )
    
    df['converted_to_pro'] = (score > np.percentile(score, 85)).astype(int)
    
    os.makedirs('csv', exist_ok=True)
    df.to_csv('csv/users_data.csv', index=False)

if __name__ == "__main__":
    generate_dataset()