import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def plot_data(genre_counts, decade_counts):

    """
    Plot data visualizations for genre popularity and movie distribution per decade.

    Parameters:
        genre_counts (pd.Series): Top genre counts.
        decade_counts (pd.Series): Movie counts per decade.
    """

    plt.figure(figsize=(10, 5))
    genre_counts.plot(kind='bar', color='teal')
    plt.title('Top 10 Movie Genres')
    plt.xlabel('Genres')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot for Number of Movies per Decade
    plt.figure(figsize=(10, 5))
    decade_counts.plot(kind='bar', color='coral')
    plt.title('Number of Movies per Decade')
    plt.xlabel('Decade')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()