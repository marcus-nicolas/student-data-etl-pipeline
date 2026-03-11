import pandas as pd

def extract_data(file_path):
    print(f"--- Starting Extraction from {file_path} ---")
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully extracted {len(df)} records.")
        return df
    except Exception as e:
        print(f"Error during extraction: {e}")
        return None