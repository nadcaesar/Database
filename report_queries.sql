-- Active: 1776191145262@@127.0.0.1@3306@gradebook

-- ============================================================
-- REPORT QUERIES — Run this file to generate all output
-- for the written report (screenshots of each section)
-- ============================================================

USE gradebook;

-- ============================================================
-- SECTION: TABLE CONTENTS (Task 3 — Sample Data)
-- ============================================================

SELECT 'PROFESSOR TABLE' AS '';
SELECT * FROM Professor;

SELECT 'COURSE TABLE' AS '';
SELECT * FROM Course;

SELECT 'CATEGORY TABLE' AS '';
SELECT * FROM Category;

SELECT 'ASSIGNMENT TABLE' AS '';
SELECT * FROM Assignment;

SELECT 'STUDENT TABLE' AS '';
SELECT * FROM Student;

SELECT 'ENROLLMENT TABLE' AS '';
SELECT * FROM Enrollment;

SELECT 'SUBMISSION TABLE' AS '';
SELECT * FROM Submission;


-- ============================================================
-- TASK 4: Average / Highest / Lowest score per assignment
-- ============================================================

SELECT 'TASK 4 — Assignment Statistics' AS '';
SELECT
    a.assignment_name,
    ROUND(AVG(s.score), 2)  AS avg_score,
    MAX(s.score)             AS highest_score,
    MIN(s.score)             AS lowest_score,
    COUNT(s.score)           AS num_submissions
FROM Submission s
JOIN Assignment a ON s.assignment_id = a.assignment_id
GROUP BY a.assignment_id, a.assignment_name
ORDER BY a.assignment_id;


-- ============================================================
-- TASK 5: All students in each course
-- ============================================================

SELECT 'TASK 5 — Students in CS101 (course_id = 1)' AS '';
SELECT
    st.student_id,
    st.first_name,
    st.last_name,
    st.email
FROM Student st
JOIN Enrollment e ON st.student_id = e.student_id
WHERE e.course_id = 1
ORDER BY st.last_name, st.first_name;

SELECT 'TASK 5 — Students in CS201 (course_id = 2)' AS '';
SELECT
    st.student_id,
    st.first_name,
    st.last_name,
    st.email
FROM Student st
JOIN Enrollment e ON st.student_id = e.student_id
WHERE e.course_id = 2
ORDER BY st.last_name, st.first_name;


-- ============================================================
-- TASK 6: All students + all scores in a course
-- ============================================================

SELECT 'TASK 6 — All Students and Scores in CS101 (course_id = 1)' AS '';
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
LEFT JOIN Submission sub ON st.student_id  = sub.student_id
                        AND a.assignment_id = sub.assignment_id
WHERE e.course_id = 1
ORDER BY st.last_name, st.first_name, cat.category_name, a.assignment_name;


-- ============================================================
-- TASK 7: Add an assignment (Homework 6) to CS101
-- ============================================================

SELECT 'TASK 7 — Before: Assignments in CS101 Homework category' AS '';
SELECT a.assignment_id, a.assignment_name, a.max_points
FROM Assignment a
JOIN Category cat ON a.category_id = cat.category_id
WHERE cat.course_id = 1 AND cat.category_name = 'Homework';

INSERT IGNORE INTO Assignment (category_id, assignment_name, max_points)
VALUES (2, 'Homework 6', 100);

SELECT 'TASK 7 — After: Homework 6 added' AS '';
SELECT a.assignment_id, a.assignment_name, a.max_points
FROM Assignment a
JOIN Category cat ON a.category_id = cat.category_id
WHERE cat.course_id = 1 AND cat.category_name = 'Homework';


-- ============================================================
-- TASK 8: Change category weights for CS101
-- ============================================================

SELECT 'TASK 8 — Before: Category weights for CS101' AS '';
SELECT category_name, weight_pct FROM Category WHERE course_id = 1;

UPDATE Category SET weight_pct = 55.00 WHERE course_id = 1 AND category_name = 'Tests';
UPDATE Category SET weight_pct = 15.00 WHERE course_id = 1 AND category_name = 'Projects';

SELECT 'TASK 8 — After: Updated weights (Tests→55%, Projects→15%)' AS '';
SELECT category_name, weight_pct FROM Category WHERE course_id = 1;

SELECT 'TASK 8 — Verify weights sum to 100' AS '';
SELECT course_id, SUM(weight_pct) AS total_weight FROM Category WHERE course_id = 1;


-- ============================================================
-- TASK 9: Add 2 points to ALL students on Midterm Exam
-- ============================================================

SELECT 'TASK 9 — Before: Midterm Exam scores (assignment_id = 8)' AS '';
SELECT st.first_name, st.last_name, sub.score
FROM Submission sub
JOIN Student st ON sub.student_id = st.student_id
WHERE sub.assignment_id = 8
ORDER BY st.last_name;

UPDATE Submission s
JOIN Assignment a ON s.assignment_id = a.assignment_id
SET s.score = LEAST(s.score + 2, a.max_points)
WHERE s.assignment_id = 8;

SELECT 'TASK 9 — After: +2 points added to all students' AS '';
SELECT st.first_name, st.last_name, sub.score
FROM Submission sub
JOIN Student st ON sub.student_id = st.student_id
WHERE sub.assignment_id = 8
ORDER BY st.last_name;


-- ============================================================
-- TASK 10: Add 2 points ONLY to students with 'Q' in last name
-- ============================================================

SELECT "TASK 10 — Before: Scores for students with 'Q' in last name" AS '';
SELECT st.first_name, st.last_name, sub.score
FROM Submission sub
JOIN Student st ON sub.student_id = st.student_id
WHERE sub.assignment_id = 8 AND st.last_name LIKE '%Q%'
ORDER BY st.last_name;

UPDATE Submission s
JOIN Student    st ON s.student_id    = st.student_id
JOIN Assignment a  ON s.assignment_id = a.assignment_id
SET s.score = LEAST(s.score + 2, a.max_points)
WHERE s.assignment_id = 8
  AND st.last_name LIKE '%Q%';

SELECT "TASK 10 — After: +2 points only for 'Q' students" AS '';
SELECT st.first_name, st.last_name, sub.score
FROM Submission sub
JOIN Student st ON sub.student_id = st.student_id
WHERE sub.assignment_id = 8
ORDER BY st.last_name;


-- ============================================================
-- TASK 11: Final grade for every student in CS101
-- ============================================================

SELECT 'TASK 11 — Final Grade for All Students in CS101' AS '';
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
    GROUP BY sub.student_id, a.category_id, cat.weight_pct
) AS graded
JOIN Student st ON graded.student_id = st.student_id
JOIN Course  c  ON c.course_id = 1
GROUP BY st.student_id, st.first_name, st.last_name, c.course_name
ORDER BY final_grade DESC;


-- ============================================================
-- TASK 12: Final grade dropping the lowest score per category
-- ============================================================

SELECT 'TASK 12 — Final Grade (Drop Lowest per Category) for All Students in CS101' AS '';
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
ORDER BY final_grade_drop_lowest DESC;
