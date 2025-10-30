import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Not Rated')

    if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    if 'date_added' in df.columns:
        df['year_added'] = df['date_added'].dt.year
    return df