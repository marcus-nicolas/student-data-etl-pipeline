import pandas as pd
import logging

def transform_data(df):
    logging.info("Starting Transformation stage.") # Part of your Logging System
    
    # 1. Fill missing GPA with the average of the group (Aggregating GPA)
    df['gpa'] = pd.to_numeric(df['gpa'], errors='coerce') # Ensure GPA is numeric
    df['gpa'] = df['gpa'].fillna(df['gpa'].mean())
    
    # 2. Standardize Gender (Fill missing with 'U' for Unknown)
    df['gender'] = df['gender'].fillna('U').str.upper()
    
    # 3. Standardize formats: Fixes mixed formats like 08/15/2003 or 2003-05-12
    df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    logging.info("Transformation complete: Cleaned missing values and standardized formats.")
    return df