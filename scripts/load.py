from sqlalchemy import create_engine, text
from config import DB_URI
import logging

def load_to_db(df, table_name):
    logging.info(f"Connecting to database to load {table_name}.")
    try:
        engine = create_engine(DB_URI)
        
        # 1. Load the main cleaned table
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"Successfully loaded {len(df)} records into {table_name}.")

        # 2. Generate Summary Table (Average GPA per Gender)
        with engine.connect() as conn:
            conn.execute(text("DROP TABLE IF EXISTS student_summary;"))
            summary_query = """
                CREATE TABLE student_summary AS
                SELECT 
                    gender, 
                    COUNT(*) as student_count, 
                    ROUND(AVG(gpa)::numeric, 2) as avg_gpa
                FROM dim_students
                GROUP BY gender;
            """
            conn.execute(text(summary_query))
            conn.commit()
            logging.info("Summary table 'student_summary' has been refreshed.")
            
    except Exception as e:
        logging.error(f"Database Load Error: {e}")
        print(f"Error: {e}")