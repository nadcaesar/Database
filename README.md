
# Grade Book Database — README
---

## Group members 

Brian Kiprop Too 
Michael Cobbins 
Nicholas Caesar

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
- **MySQL 8.0+** (or MariaDB 10.5+)
- **Python 3.8+**
- Python package: `mysql-connector-python`

---

## Setup Instructions

### Step 1 — Install Python dependency
```bash
pip install mysql-connector-python
```

### Step 2 — Start MySQL and load the database
```bash
mysql -u root -p < gradebook.sql
```
This creates the `gradebook` database, all tables, and inserts sample data.

### Step 3 — Configure your credentials
Open `gradebook.py` and edit the `DB_CONFIG` block at the top:
```python
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",        # your MySQL username
    "password": "yourpassword",# your MySQL password
    "database": "gradebook"
}
```

### Step 4 — Run the program
mysql terminal: 
```bash
source gradebook.sql
```
powershell terminal:
```bash
python gradebook.py
```
You will see a menu. Type a task number (1-9) and press Enter.

---

## Test Cases

### Task 4 — Assignment stats
Input: assignment_id = 3 (Homework 1)
Expected: avg ~85.0, highest 95, lowest 72

### Task 5 — List students in course
Input: course_id = 1
Expected: 8 students listed (Johnson, Smith, Quinones, Brown, Quinn, Lee, Martinez, Qiu)

### Task 9 — Add 2 points all students
Input: assignment_id = 8 (Midterm)
Expected: all scores increase by 2, capped at 100

### Task 10 — Add 2 points Q-students
Input: assignment_id = 8
Expected: Only Quinones, Quinn, Qiu receive +2

### Task 11 — Student grade
Input: student_id=1, course_id=1
Expected: ~90+ (Alice has high scores across all categories)

### Task 12 — Drop lowest
Input: student_id=1, course_id=1
Expected: grade slightly higher than Task 11 (worst score per category removed)
