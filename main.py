import logging
import os
import pandas as pd
from sqlalchemy import create_engine, text
from config import RAW_DATA_PATH, LOG_FILE_PATH, DB_URI
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_to_db

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def verify_results():
    """Checks the database to confirm data was loaded correctly."""
    print("\n--- Starting Verification ---")
    try:
        engine = create_engine(DB_URI)
        with engine.connect() as conn:
            # Check main dimension table
            result = conn.execute(text("SELECT COUNT(*) FROM dim_students"))
            count = result.scalar()
            print(f"Verification: {count} records found in 'dim_students'.")
            
            # Check summary table
            summary = conn.execute(text("SELECT * FROM student_summary"))
            print("\n--- Student Summary (PostgreSQL) ---")
            for row in summary:
                # row[0] is gender, row[1] is average_gpa
                gender_label = row[0] if row[0] else "Not Specified"
                avg_gpa = row[1] if row[1] is not None else 0.0
                print(f"Gender Group: {gender_label} | Avg GPA: {avg_gpa:.2f}")
    except Exception as e:
        print(f"Verification note: {e}")

def run_pipeline():
    logging.info("--- ETL Pipeline Session Started ---")
    print("Starting ETL Pipeline...")
    
    # 1. Extract
    # This pulls from N:\student-data-etl-pipeline\data\raw\students.csv
    data = extract_data(RAW_DATA_PATH)
    
    if data is not None:
        # 2. Transform
        # This handles your birth_date formatting logic
        clean_data = transform_data(data)
        
        # Standardize column names to prevent KeyErrors
        clean_data.columns = clean_data.columns.str.strip().str.lower()
        
        # 3. Load Main Table (dim_students)
        load_to_db(clean_data, 'dim_students')
        
        # 4. Create and Load Summary Table
        # Groups by gender to calculate average GPA. 
        # dropna=False ensures we see a group for missing gender values.
        summary_df = clean_data.groupby('gender', dropna=False)['gpa'].mean().reset_index()
        summary_df.columns = ['gender', 'average_gpa']
        
        load_to_db(summary_df, 'student_summary')
        
        print("Pipeline finished! Check logs/pipeline.log and your Postgres database.")
        
        # 5. Automated Verification
        verify_results()
    
    logging.info("--- ETL Pipeline Session Finished ---")

if __name__ == "__main__":
    run_pipeline()