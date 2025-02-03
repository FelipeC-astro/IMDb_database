def analyze_data(df):
    genre_counts = df['genres'].str.split(',', expand=True).stack().value_counts().head(10)
    decade_counts = df.assign(decade=(df['startYear'] // 10) * 10)['decade'].value_counts().sort_index()
    return genre_counts, decade_counts