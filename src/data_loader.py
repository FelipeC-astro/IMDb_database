def load_data(filepath):
    import pandas as pd
    try:
        df = pd.read_csv(filepath, sep='\t', low_memory=False)
        print(f'Dataset carregado com sucesso! {df.shape[0]} linhas e {df.shape[1]} colunas.')
        return df
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho.")