
# Grade Book Database — README
---

## Group members 

- Brian Kiprop Too 
- Michael Cobbins 
- Nicholas Caesar

---

## Project Overview   
A MySQL-backed grade book that allows a professor to manage courses,
grading categories, assignments, students, and scores. Supports grade
computation including a "drop lowest" mode per category.

---

## Files
| File | Description |
|---|---|
| `gradebook.sql` | Full SQL: schema creation, sample data, and all task queries |
| `gradebook.py` | Python menu-driven interface for Tasks 4–12 |


---

## Requirements
- MySQL 8.0 or newer
- Python 3.8 or newer
- Python package: `mysql-connector-python`

---

## Setup Instructions

### Step 1 — Install Python dependency
```bash
pip install mysql-connector-python
```

### Step 2 — Load the database
Open the MySQL command line client and run:
```sql
source gradebook.sql
```

### Step 3 — Update credentials in gradebook.py
Open `gradebook.py` and update `DB_CONFIG` with your MySQL username and password:
```python
DB_CONFIG = {
    "host":     "localhost",
    "user":     "your_username",
    "password": "your_password",
    "database": "gradebook"
}
```

### Step 4 — Run the program
```bash
python gradebook.py
```
