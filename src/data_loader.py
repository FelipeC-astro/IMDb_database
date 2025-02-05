import pandas as pd

def load_data(filepath):
    """
    Load IMDb dataset from a TSV file.

    Parameters:
        filepath (str): Path to the dataset file.

    Returns:
        pd.DataFrame: Loaded dataset as a DataFrame.
    """
    try:
        df = pd.read_csv(filepath, sep='\t', low_memory=False)
        print(f'Dataset loaded successfully! {df.shape[0]} rows and {df.shape[1]} columns.')
        return df
    except FileNotFoundError:
        print("File not found. Check the path.")
        return None