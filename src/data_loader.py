def load_data(filepath):
    import pandas as pd
    try:
        df = pd.read_csv(filepath, sep='\t', low_memory=False)
        print(f'Dataset loaded successfully! {df.shape[0]} rows and {df.shape[1]} columns.')
        return df
    except FileNotFoundError:
        print("File not found. Check the path.")