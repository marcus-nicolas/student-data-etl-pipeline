# Student Data ETL Pipeline

## Architecture
1. **Extract**: Reads raw student profiles from `students.csv`.
2. **Transform**: Python (Pandas) cleans null GPAs and standardizes date formats.
3. **Load**: Data is pushed to PostgreSQL; a secondary SQL script generates a `student_summary` table.

## Tech Stack
* **Language**: Python 3.x
* **Data Handling**: Pandas
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy

## How to Run
1. Activate venv: `.\venv\Scripts\activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`