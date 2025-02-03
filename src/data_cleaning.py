import pandas as pd

def clean_data(df):
    df = df[df['titleType'] == 'movie']  # Filter only movies
    df.dropna(subset=['startYear', 'genres'], inplace=True)  # Remove missing values
    df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')  # Convert year
    return df