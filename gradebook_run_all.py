#!/usr/bin/env python3
"""
gradebook_run_all.py
Runs every task (4-12) automatically with fixed demo values,
prints a formatted report to the console, and saves it to
gradebook_output.txt for use in your written report.
"""

import mysql.connector
from mysql.connector import Error
import sys
from io import StringIO
import contextlib

# ── Connection config ────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "ncaesar",       # change if needed
    "password": "database123",   # change if needed
    "database": "gradebook"
}

OUTPUT_FILE = "gradebook_output.txt"

# ── Output capture ───────────────────────────────────────────────
output_lines = []

def emit(text=""):
    print(text)
    output_lines.append(text)


def section(title):
    bar = "=" * 60
    emit()
    emit(bar)
    emit(f"  {title}")
    emit(bar)


def print_table(cursor):
    rows = cursor.fetchall()
    if not rows:
        emit("  (no results)")
        return
    cols = [d[0] for d in cursor.description]
    widths = [
        max(len(str(col)), max((len(str(r[i])) for r in rows), default=0))
        for i, col in enumerate(cols)
    ]
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt = "|" + "|".join(f" {{:<{w}}} " for w in widths) + "|"
    emit(sep)
    emit(fmt.format(*cols))
    emit(sep)
    for row in rows:
        emit(fmt.format(*[str(v) if v is not None else "NULL" for v in row]))
    emit(sep)
    emit(f"  {len(rows)} row(s)\n")


# ── Helpers ───────────────────────────────────────────────────────
def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"[ERROR] Cannot connect to MySQL: {e}")
        sys.exit(1)


def run(conn, sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur


# ════════════════════════════════════════════════════════════════
# TASK 4 — Assignment stats (avg / highest / lowest)
# ════════════════════════════════════════════════════════════════
def task4(conn):
    section("TASK 4 — Assignment Stats  (assignment_id = 3: Homework 1)")
    cur = run(conn, """
        SELECT
            a.assignment_name,
            ROUND(AVG(s.score), 2)  AS avg_score,
            MAX(s.score)             AS highest_score,
            MIN(s.score)             AS lowest_score,
            COUNT(s.score)           AS submissions
        FROM Submission s
        JOIN Assignment a ON s.assignment_id = a.assignment_id
        WHERE a.assignment_id = 3
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 5 — List all students in a course
# ════════════════════════════════════════════════════════════════
def task5(conn):
    section("TASK 5 — Students in Course  (course_id = 1: CS101)")
    cur = run(conn, """
        SELECT st.student_id, st.first_name, st.last_name, st.email
        FROM Student st
        JOIN Enrollment e ON st.student_id = e.student_id
        WHERE e.course_id = 1
        ORDER BY st.last_name, st.first_name
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 6 — All students + all scores in a course
# ════════════════════════════════════════════════════════════════
def task6(conn):
    section("TASK 6 — All Students & Scores  (course_id = 1: CS101)")
    cur = run(conn, """
        SELECT
            st.first_name,
            st.last_name,
            cat.category_name,
            a.assignment_name,
            sub.score,
            a.max_points
        FROM Student st
        JOIN Enrollment  e   ON st.student_id    = e.student_id
        JOIN Category    cat ON e.course_id      = cat.course_id
        JOIN Assignment  a   ON cat.category_id  = a.category_id
        LEFT JOIN Submission sub
               ON st.student_id = sub.student_id
              AND a.assignment_id = sub.assignment_id
        WHERE e.course_id = 1
        ORDER BY st.last_name, cat.category_name, a.assignment_name
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 7 — Add an assignment to a course
# ════════════════════════════════════════════════════════════════
def task7(conn):
    section("TASK 7 — Add Assignment  ('Homework 6' to CS101 Homework, category_id=2)")

    # Check if Homework 6 was already added in a previous run to keep idempotent
    cur = run(conn,
        "SELECT assignment_id FROM Assignment WHERE assignment_name = 'Homework 6' AND category_id = 2")
    existing = cur.fetchone()
    cur.close()

    if existing:
        new_id = existing[0]
        emit(f"  (Homework 6 already exists as assignment_id={new_id}, skipping INSERT)")
    else:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Assignment (category_id, assignment_name, max_points) VALUES (2, 'Homework 6', 100)")
        conn.commit()
        new_id = cur.lastrowid
        emit(f"  Assignment 'Homework 6' inserted with assignment_id = {new_id}")

        # Insert blank submissions for all students enrolled in course 1
        cur.execute("SELECT student_id FROM Enrollment WHERE course_id = 1")
        students = cur.fetchall()
        for (sid,) in students:
            cur.execute(
                "INSERT IGNORE INTO Submission (student_id, assignment_id, score) VALUES (%s, %s, NULL)",
                (sid, new_id))
        conn.commit()
        emit(f"  Blank submissions created for {len(students)} enrolled students.")
        cur.close()

    # Show updated assignment list for course 1
    cur = run(conn, """
        SELECT a.assignment_id, a.assignment_name, a.max_points, cat.category_name
        FROM Assignment a
        JOIN Category cat ON a.category_id = cat.category_id
        WHERE cat.course_id = 1
        ORDER BY cat.category_name, a.assignment_id
    """)
    emit("\n  Current assignments for CS101:")
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 8 — Change category weights for a course
# ════════════════════════════════════════════════════════════════
def task8(conn):
    section("TASK 8 — Update Category Weights  (CS101: Tests 55%, Projects 15%)")
    emit("  Before update:")
    cur = run(conn, "SELECT category_name, weight_pct FROM Category WHERE course_id = 1")
    print_table(cur)
    cur.close()

    cur = conn.cursor()
    cur.execute("UPDATE Category SET weight_pct = 55.00 WHERE course_id = 1 AND category_name = 'Tests'")
    cur.execute("UPDATE Category SET weight_pct = 15.00 WHERE course_id = 1 AND category_name = 'Projects'")
    conn.commit()
    cur.close()

    emit("  After update:")
    cur = run(conn, "SELECT category_name, weight_pct FROM Category WHERE course_id = 1")
    print_table(cur)

    cur2 = run(conn, "SELECT SUM(weight_pct) AS total_weight FROM Category WHERE course_id = 1")
    emit("  Weight sum verification:")
    print_table(cur2)
    cur.close()
    cur2.close()


# ════════════════════════════════════════════════════════════════
# TASK 9 — Add 2 points to ALL students on one assignment
# ════════════════════════════════════════════════════════════════
def task9(conn):
    section("TASK 9 — Add 2 Points to All Students  (assignment_id = 8: Midterm Exam)")
    emit("  Scores BEFORE:")
    cur = run(conn, """
        SELECT st.first_name, st.last_name, s.score
        FROM Submission s
        JOIN Student st ON s.student_id = st.student_id
        WHERE s.assignment_id = 8
        ORDER BY st.last_name
    """)
    print_table(cur)
    cur.close()

    cur = conn.cursor()
    cur.execute("""
        UPDATE Submission s
        JOIN Assignment a ON s.assignment_id = a.assignment_id
        SET s.score = LEAST(s.score + 2, a.max_points)
        WHERE s.assignment_id = 8 AND s.score IS NOT NULL
    """)
    conn.commit()
    rows_affected = cur.rowcount
    cur.close()
    emit(f"  Rows updated: {rows_affected}")

    emit("\n  Scores AFTER:")
    cur = run(conn, """
        SELECT st.first_name, st.last_name, s.score
        FROM Submission s
        JOIN Student st ON s.student_id = st.student_id
        WHERE s.assignment_id = 8
        ORDER BY st.last_name
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 10 — Add 2 points only to students with 'Q' in last name
# ════════════════════════════════════════════════════════════════
def task10(conn):
    section("TASK 10 — Add 2 Points to 'Q' Students  (assignment_id = 8: Midterm Exam)")
    emit("  Students with 'Q' in last name:")
    cur = run(conn, "SELECT student_id, first_name, last_name FROM Student WHERE last_name LIKE '%Q%'")
    print_table(cur)
    cur.close()

    emit("  Scores BEFORE (Midterm Exam):")
    cur = run(conn, """
        SELECT st.first_name, st.last_name, s.score
        FROM Submission s
        JOIN Student st ON s.student_id = st.student_id
        WHERE s.assignment_id = 8
          AND st.last_name LIKE '%Q%'
        ORDER BY st.last_name
    """)
    print_table(cur)
    cur.close()

    cur = conn.cursor()
    cur.execute("""
        UPDATE Submission s
        JOIN Student    st ON s.student_id    = st.student_id
        JOIN Assignment a  ON s.assignment_id = a.assignment_id
        SET s.score = LEAST(s.score + 2, a.max_points)
        WHERE s.assignment_id = 8
          AND st.last_name LIKE '%Q%'
          AND s.score IS NOT NULL
    """)
    conn.commit()
    rows_affected = cur.rowcount
    cur.close()
    emit(f"  Rows updated: {rows_affected}")

    emit("\n  Scores AFTER (Midterm Exam, 'Q' students):")
    cur = run(conn, """
        SELECT st.first_name, st.last_name, s.score
        FROM Submission s
        JOIN Student st ON s.student_id = st.student_id
        WHERE s.assignment_id = 8
          AND st.last_name LIKE '%Q%'
        ORDER BY st.last_name
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 11 — Final grade for a student (normal, no drops)
# ════════════════════════════════════════════════════════════════
def task11(conn):
    section("TASK 11 — Final Grade (Normal)  —  All Students in CS101")
    cur = run(conn, """
        SELECT
            st.first_name,
            st.last_name,
            c.course_name,
            ROUND(SUM(cat_grade), 2) AS final_grade
        FROM (
            SELECT
                sub.student_id,
                a.category_id,
                (AVG(sub.score / a.max_points) * cat.weight_pct) AS cat_grade
            FROM Submission sub
            JOIN Assignment  a   ON sub.assignment_id = a.assignment_id
            JOIN Category    cat ON a.category_id     = cat.category_id
            WHERE cat.course_id = 1
              AND sub.score IS NOT NULL
            GROUP BY sub.student_id, a.category_id, cat.weight_pct
        ) AS graded
        JOIN Student st ON graded.student_id = st.student_id
        JOIN Course  c  ON c.course_id = 1
        GROUP BY st.student_id, st.first_name, st.last_name, c.course_name
        ORDER BY final_grade DESC
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# TASK 12 — Final grade dropping lowest score per category
# ════════════════════════════════════════════════════════════════
def task12(conn):
    section("TASK 12 — Final Grade (Drop Lowest per Category)  —  All Students in CS101")
    cur = run(conn, """
        SELECT
            st.first_name,
            st.last_name,
            c.course_name,
            ROUND(SUM(cat_grade), 2) AS final_grade_drop_lowest
        FROM (
            SELECT
                sub.student_id,
                a.category_id,
                cat.weight_pct,
                (AVG(sub.score / a.max_points) * cat.weight_pct) AS cat_grade
            FROM Submission sub
            JOIN Assignment  a   ON sub.assignment_id = a.assignment_id
            JOIN Category    cat ON a.category_id     = cat.category_id
            WHERE cat.course_id = 1
              AND sub.score IS NOT NULL
              AND sub.score > (
                  SELECT MIN(s2.score)
                  FROM Submission s2
                  JOIN Assignment a2 ON s2.assignment_id = a2.assignment_id
                  WHERE s2.student_id = sub.student_id
                    AND a2.category_id = a.category_id
              )
            GROUP BY sub.student_id, a.category_id, cat.weight_pct
        ) AS graded
        JOIN Student st ON graded.student_id = st.student_id
        JOIN Course  c  ON c.course_id = 1
        GROUP BY st.student_id, st.first_name, st.last_name, c.course_name
        ORDER BY final_grade_drop_lowest DESC
    """)
    print_table(cur)
    cur.close()


# ════════════════════════════════════════════════════════════════
# BONUS — Table snapshots for the report (Task 3 verification)
# ════════════════════════════════════════════════════════════════
def bonus_snapshots(conn):
    section("BONUS — Table Snapshots  (Task 3: verify sample data)")
    for table in ["Professor", "Course", "Category", "Assignment", "Student", "Enrollment"]:
        emit(f"\n  SELECT * FROM {table}:")
        cur = run(conn, f"SELECT * FROM {table}")
        print_table(cur)
        cur.close()


# ════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════
def main():
    header = "GRADE BOOK DATABASE — Full Demo Run"
    emit("=" * 60)
    emit(f"  {header}")
    emit("=" * 60)

    conn = get_connection()
    emit("  Connected to MySQL 'gradebook' database.\n")

    bonus_snapshots(conn)
    task4(conn)
    task5(conn)
    task6(conn)
    task7(conn)
    task8(conn)
    task9(conn)
    task10(conn)
    task11(conn)
    task12(conn)

    conn.close()

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    emit(f"\n  Output saved to '{OUTPUT_FILE}'")
    emit("  Done.")


if __name__ == "__main__":
    main()
