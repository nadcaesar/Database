# Grade Book Database — README

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
| `README.md` | This file |

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
```bash
python gradebook.py
```
You will see a menu. Type a task number (4–12) and press Enter.

---

## Database Schema

```
Professor(professor_id PK, first_name, last_name, email)
    │
    └── Course(course_id PK, professor_id FK, department,
               course_number, course_name, semester, year)
                │
                └── Category(category_id PK, course_id FK,
                              category_name, weight_pct)
                              [weights must sum to 100 per course]
                        │
                        └── Assignment(assignment_id PK, category_id FK,
                                       assignment_name, max_points)

Student(student_id PK, first_name, last_name, email)
    │
    ├── Enrollment(enrollment_id PK, student_id FK, course_id FK)
    │
    └── Submission(submission_id PK, student_id FK,
                   assignment_id FK, score)
```

**Key Design Decisions:**
- Category weights per course must sum to 100 (validated in Python)
- Each assignment belongs to exactly one category
- Submission score can be NULL (not yet graded)
- Scores are capped at `max_points` when adding bonus points

---

## Grade Calculation

### Task 11 — Normal Grade
For each category:
```
category_contribution = AVG(score / max_points) × weight_pct
```
Final grade = sum of all category contributions.

### Task 12 — Drop Lowest
Same as Task 11, but the single lowest score in each category is
excluded from the average before computing the contribution.

---

## Sample Data Summary
- **1 Professor**: Maria Liu
- **2 Courses**: CS101 (Fall 2024), CS201 (Spring 2025)
- **8 Students**: includes Quinones, Quinn, and Qiu (for Task 10 testing)
- **~10 Assignments** across CS101, **~7** in CS201
- **Complete submissions** for all students in CS101

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
