def plot_data(genre_counts, decade_counts):
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 5))
    genre_counts.plot(kind='bar', color='teal')
    plt.title('Top 10 Gêneros de Filmes')
    plt.show()

    plt.figure(figsize=(10, 5))
    decade_counts.plot(kind='bar', color='coral')
    plt.title('Número de Filmes por Década')
    plt.show()