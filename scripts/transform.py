# Standardizing date formats and handling missing values to ensure data integrity.
import pandas as pd
import logging

def transform_data(df):
    logging.info("Starting Transformation stage.")
    

    df['gpa'] = pd.to_numeric(df['gpa'], errors='coerce')
    df['gpa'] = df['gpa'].fillna(df['gpa'].mean())
    

    df['gender'] = df['gender'].fillna('U').str.upper()
    

    df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    logging.info("Transformation complete: Cleaned missing values and standardized formats.")
    return df