from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_data

def main():
    
    filepath = 'data/title.basics.tsv'  # File path
    df = load_data(filepath)

    if df is not None:  # Check if data was loaded successfully
        df_clean = clean_data(df)
        genre_counts, decade_counts = analyze_data(df_clean)
        plot_data(genre_counts, decade_counts)
    else:
        print("Data loading failed. Exiting the program.")

if __name__ == '__main__':
    main()
