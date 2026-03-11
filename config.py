# PostgreSQL Connection Details
DB_USER = "postgres"
DB_PASS = "admin123"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "student_pipeline_db"

# Connection String (SQLAlchemy format)
DB_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# File Paths for your folder structure
RAW_DATA_PATH = "data/raw/students.csv"
LOG_FILE_PATH = "logs/pipeline.log"