def clean_data(df):
    df = df[df['titleType'] == 'movie']  # Filtra apenas filmes
    df.dropna(subset=['startYear', 'genres'], inplace=True)  # Remove valores ausentes
    df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')  # Converte o ano
    return df