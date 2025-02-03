from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_data

def main():
    filepath = 'data/imdb_dataset.tsv'  # file path
    df = load_data(filepath)
    df_clean = clean_data(df)
    genre_counts, decade_counts = analyze_data(df_clean)
    plot_data(genre_counts, decade_counts)

if __name__ == '__main__':
    main()