"""
gradebook.py
Grade Book Database — Python interface
Database Project

Requirements:
    pip install mysql-connector-python
    MySQL running with gradebook.sql loaded first.
"""

import mysql.connector
from mysql.connector import Error
import sys

# ── Connection config ────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "ncaesar",        # change to your MySQL username
    "password": "database123",            # change to your MySQL password
    "database": "gradebook"
}


def get_connection():
    """Return a MySQL connection or exit on failure."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"[ERROR] Could not connect to MySQL: {e}")
        sys.exit(1)


def print_results(cursor):
    """Pretty-print all rows from the last query."""
    rows = cursor.fetchall()
    if not rows:
        print("  (no results)")
        return
    cols = [d[0] for d in cursor.description]
    widths = [max(len(str(col)), max((len(str(r[i])) for r in rows), default=0))
              for i, col in enumerate(cols)]
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt = "|" + "|".join(f" {{:<{w}}} " for w in widths) + "|"
    print(sep)
    print(fmt.format(*cols))
    print(sep)
    for row in rows:
        print(fmt.format(*[str(v) if v is not None else "NULL" for v in row]))
    print(sep)
    print(f"  {len(rows)} row(s) returned.\n")


# ════════════════════════════════════════════════════════════════
# TASK 4 — Average / Highest / Lowest score of an assignment
# ════════════════════════════════════════════════════════════════
def task4_assignment_stats(conn):
    cursor = conn.cursor()
    # Show available assignments first
    cursor.execute("SELECT assignment_id, assignment_name FROM Assignments ORDER BY assignment_id")
    print("\nAvailable Assignments:")
    print_results(cursor)
    aid = int(input("Enter assignment_id to get stats: "))
    cursor.execute("""
        SELECT
            a.assignment_name,
            ROUND(AVG(s.score), 2)  AS avg_score,
            MAX(s.score)             AS highest_score,
            MIN(s.score)             AS lowest_score,
            COUNT(s.score)           AS submissions
        FROM Submission s
        JOIN Assignments a ON s.assignment_id = a.assignment_id
        WHERE a.assignment_id = %s
    """, (aid,))
    print_results(cursor)
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 5 — List all students in a course
# ════════════════════════════════════════════════════════════════
def task5_students_in_course(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name, semester, year FROM Course")
    print("\nAvailable Courses:")
    print_results(cursor)
    cid = int(input("Enter course_id: "))
    cursor.execute("""
        SELECT st.student_id, st.first_name, st.last_name, st.email
        FROM Student st
        JOIN Enrollment e ON st.student_id = e.student_id
        WHERE e.course_id = %s
        ORDER BY st.last_name, st.first_name
    """, (cid,))
    print_results(cursor)
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 6 — All students + all scores in a course
# ════════════════════════════════════════════════════════════════
def task6_all_scores(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name FROM Course")
    print("\nAvailable Courses:")
    print_results(cursor)
    cid = int(input("Enter course_id: "))
    cursor.execute("""
        SELECT
            st.first_name, st.last_name,
            cat.category_name,
            a.assignment_name,
            sub.score,
            a.max_points
        FROM Student st
        JOIN Enrollment  e   ON st.student_id    = e.student_id
        JOIN Category    cat ON e.course_id      = cat.course_id
        JOIN Assignments a   ON cat.category_id  = a.category_id
        LEFT JOIN Submission sub ON st.student_id = sub.student_id
                                AND a.assignment_id = sub.assignment_id
        WHERE e.course_id = %s
        ORDER BY st.last_name, cat.category_name, a.assignment_name
    """, (cid,))
    print_results(cursor)
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 7 — Add an assignment to a course
# ════════════════════════════════════════════════════════════════
def task7_add_assignment(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name FROM Course")
    print("\nAvailable Courses:")
    print_results(cursor)
    cid = int(input("Enter course_id to add assignment to: "))

    cursor.execute("SELECT category_id, category_name FROM Category WHERE course_id = %s", (cid,))
    print("\nCategories for this course:")
    print_results(cursor)
    cat_id = int(input("Enter category_id for the new assignment: "))

    name = input("Assignment name: ").strip()
    pts  = float(input("Max points (default 100): ") or "100")

    cursor.execute("""
        INSERT INTO Assignments (category_id, assignment_name, max_points)
        VALUES (%s, %s, %s)
    """, (cat_id, name, pts))
    conn.commit()
    new_id = cursor.lastrowid
    print(f"\n   Assignment '{name}' added with assignment_id = {new_id}")

    # Optionally insert blank submissions for all enrolled students
    cursor.execute("""
        SELECT student_id FROM Enrollment WHERE course_id = %s
    """, (cid,))
    students = cursor.fetchall()
    for (sid,) in students:
        cursor.execute("""
            INSERT IGNORE INTO Submission (student_id, assignment_id, score)
            VALUES (%s, %s, NULL)
        """, (sid, new_id))
    conn.commit()
    print(f"   Blank submissions created for {len(students)} enrolled students.\n")
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 8 — Change category weights for a course
# ════════════════════════════════════════════════════════════════
def task8_change_weights(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name FROM Course")
    print("\nAvailable Courses:")
    print_results(cursor)
    cid = int(input("Enter course_id: "))

    cursor.execute("""
        SELECT category_id, category_name, weight_pct
        FROM Category WHERE course_id = %s
    """, (cid,))
    print("\nCurrent Categories and Weights:")
    print_results(cursor)

    cursor.execute("SELECT category_id, category_name FROM Category WHERE course_id = %s", (cid,))
    categories = cursor.fetchall()
    total = 0.0
    updates = []
    print("Enter new weights (must sum to 100):")
    for cat_id, cat_name in categories:
        w = float(input(f"  {cat_name} weight %: "))
        updates.append((w, cat_id))
        total += w

    if abs(total - 100.0) > 0.01:
        print(f"  Weights sum to {total:.2f}, not 100. No changes made.")
        return

    for (w, cat_id) in updates:
        cursor.execute("UPDATE Category SET weight_pct = %s WHERE category_id = %s", (w, cat_id))
    conn.commit()
    print("  Weights updated successfully.\n")
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 9 — Add 2 points to ALL students on an assignment
# ════════════════════════════════════════════════════════════════
def task9_add_points_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT assignment_id, assignment_name, max_points FROM Assignments ORDER BY assignment_id")
    print("\nAvailable Assignments:")
    print_results(cursor)
    aid = int(input("Enter assignment_id to add 2 points to (all students): "))
    pts = float(input("Points to add (default 2): ") or "2")

    cursor.execute("""
        UPDATE Submission s
        JOIN Assignments a ON s.assignment_id = a.assignment_id
        SET s.score = LEAST(s.score + %s, a.max_points)
        WHERE s.assignment_id = %s AND s.score IS NOT NULL
    """, (pts, aid))
    conn.commit()
    print(f"  Added {pts} points to {cursor.rowcount} submission(s), capped at max_points.\n")
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 10 — Add 2 points ONLY to students whose last name has 'Q'
# ════════════════════════════════════════════════════════════════
def task10_add_points_q(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT assignment_id, assignment_name, max_points FROM Assignments ORDER BY assignment_id")
    print("\nAvailable Assignments:")
    print_results(cursor)
    aid = int(input("Enter assignment_id (only students with 'Q' in last name get +2): "))
    pts = float(input("Points to add (default 2): ") or "2")

    cursor.execute("""
        UPDATE Submission s
        JOIN Student    st ON s.student_id    = st.student_id
        JOIN Assignments a  ON s.assignment_id = a.assignment_id
        SET s.score = LEAST(s.score + %s, a.max_points)
        WHERE s.assignment_id = %s
          AND st.last_name LIKE '%Q%'
          AND s.score IS NOT NULL
    """, (pts, aid))
    conn.commit()
    print(f"  Added {pts} points to {cursor.rowcount} student(s) with 'Q' in last name.\n")
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 11 — Compute final grade for a student (normal)
# ════════════════════════════════════════════════════════════════
def task11_student_grade(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, first_name, last_name FROM Student ORDER BY student_id")
    print("\nStudents:")
    print_results(cursor)
    sid = int(input("Enter student_id: "))

    cursor.execute("SELECT course_id, course_name FROM Course")
    print("\nCourses:")
    print_results(cursor)
    cid = int(input("Enter course_id: "))

    cursor.execute("""
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
            JOIN Assignments a   ON sub.assignment_id = a.assignment_id
            JOIN Category    cat ON a.category_id     = cat.category_id
            WHERE cat.course_id = %s AND sub.student_id = %s
            GROUP BY sub.student_id, a.category_id, cat.weight_pct
        ) AS graded
        JOIN Student st ON graded.student_id = st.student_id
        JOIN Course  c  ON c.course_id = %s
        GROUP BY st.student_id, st.first_name, st.last_name, c.course_name
    """, (cid, sid, cid))
    print_results(cursor)
    cursor.close()


# ════════════════════════════════════════════════════════════════
# TASK 12 — Grade for a student, dropping the lowest per category
# ════════════════════════════════════════════════════════════════
def task12_grade_drop_lowest(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, first_name, last_name FROM Student ORDER BY student_id")
    print("\nStudents:")
    print_results(cursor)
    sid = int(input("Enter student_id: "))

    cursor.execute("SELECT course_id, course_name FROM Course")
    print("\nCourses:")
    print_results(cursor)
    cid = int(input("Enter course_id: "))

    cursor.execute("""
        SELECT
            st.first_name,
            st.last_name,
            c.course_name,
            ROUND(SUM(cat_grade), 2) AS final_grade_drop_lowest
        FROM (
            SELECT
                ranked.student_id,
                ranked.category_id,
                cat.weight_pct,
                (AVG(ranked.score / ranked.max_points) * cat.weight_pct) AS cat_grade
            FROM (
                SELECT
                    sub.student_id,
                    sub.score,
                    a.max_points,
                    a.category_id,
                    ROW_NUMBER() OVER (
                        PARTITION BY sub.student_id, a.category_id
                        ORDER BY sub.score ASC
                    ) AS rn,
                    COUNT(*) OVER (
                        PARTITION BY sub.student_id, a.category_id
                    ) AS total_in_cat
                FROM Submission sub
                JOIN Assignments a   ON sub.assignment_id = a.assignment_id
                JOIN Category    cat ON a.category_id     = cat.category_id
                WHERE cat.course_id = %s
                  AND sub.student_id = %s
                  AND sub.score IS NOT NULL
            ) AS ranked
            JOIN Category cat ON ranked.category_id = cat.category_id
            WHERE ranked.rn > 1 OR ranked.total_in_cat = 1
            GROUP BY ranked.student_id, ranked.category_id, cat.weight_pct
        ) AS graded
        JOIN Student st ON graded.student_id = st.student_id
        JOIN Course  c  ON c.course_id = %s
        GROUP BY st.student_id, st.first_name, st.last_name, c.course_name
    """, (cid, sid, cid))
    print_results(cursor)
    cursor.close()


# ════════════════════════════════════════════════════════════════
# MAIN MENU
# ════════════════════════════════════════════════════════════════
MENU = """
╔══════════════════════════════════════════════════╗
║          GRADE BOOK DATABASE — MENU              ║
╠══════════════════════════════════════════════════╣
║   4.  Assignment stats (avg / high / low)        ║
║   5.  List students in a course                  ║
║   6.  All students + all scores in a course      ║
║   7.  Add an assignment to a course              ║
║   8.  Change category weights for a course       ║
║   9.  Add points to all students on assignment   ║
║  10.  Add points to students with 'Q' in name   ║
║  11.  Compute a student's final grade            ║
║  12.  Grade with lowest score dropped per cat.   ║
║   q.  Quit                                       ║
╚══════════════════════════════════════════════════╝
"""

TASKS = {
    "4":  task4_assignment_stats,
    "5":  task5_students_in_course,
    "6":  task6_all_scores,
    "7":  task7_add_assignment,
    "8":  task8_change_weights,
    "9":  task9_add_points_all,
    "10": task10_add_points_q,
    "11": task11_student_grade,
    "12": task12_grade_drop_lowest,
}

def main():
    print("\n  Connecting to Grade Book Database...")
    conn = get_connection()
    print("Connected.\n")

    while True:
        print(MENU)
        choice = input("Enter task number: ").strip().lower()
        if choice == "q":
            print("  Goodbye!")
            break
        elif choice in TASKS:
            try:
                TASKS[choice](conn)
            except Error as e:
                print(f"  [DB ERROR] {e}\n")
            except ValueError:
                print("  [INPUT ERROR] Please enter a valid number.\n")
        else:
            print("  Invalid choice. Please try again.\n")

    conn.close()


if __name__ == "__main__":
    main()
