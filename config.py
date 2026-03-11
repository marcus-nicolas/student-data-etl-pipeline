DB_USER = "postgres"
DB_PASS = "admin123"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "student_pipeline_db"


DB_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


RAW_DATA_PATH = "data/raw/students.csv"
LOG_FILE_PATH = "logs/pipeline.log"