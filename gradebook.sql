-- ============================================================
--  GRADE BOOK DATABASE
--  Database Project — MySQL
-- ============================================================

DROP DATABASE IF EXISTS gradebook;
CREATE DATABASE gradebook;
USE gradebook;

-- ============================================================
-- TABLE CREATION (Task 2)
-- ============================================================

-- Professor who teaches courses
CREATE TABLE Professor (
    professor_id   INT          AUTO_INCREMENT PRIMARY KEY,
    first_name     VARCHAR(50)  NOT NULL,
    last_name      VARCHAR(50)  NOT NULL,
    email          VARCHAR(100) UNIQUE
);

-- Course offered by a professor
CREATE TABLE Course (
    course_id      INT          AUTO_INCREMENT PRIMARY KEY,
    professor_id   INT          NOT NULL,
    department     VARCHAR(50)  NOT NULL,
    course_number  VARCHAR(20)  NOT NULL,
    course_name    VARCHAR(100) NOT NULL,
    semester       ENUM('Spring','Summer','Fall','Winter') NOT NULL,
    year           YEAR         NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES Professor(professor_id)
);

-- Grading categories per course (homework, tests, projects, etc.)
-- Weights must sum to 100 per course — enforced in application logic
CREATE TABLE Category (
    category_id    INT          AUTO_INCREMENT PRIMARY KEY,
    course_id      INT          NOT NULL,
    category_name  VARCHAR(50)  NOT NULL,
    weight_pct     DECIMAL(5,2) NOT NULL,   -- e.g. 20.00 means 20%
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    UNIQUE (course_id, category_name)
);

-- Individual assignments belonging to a category
CREATE TABLE Assignments (
    assignment_id   INT          AUTO_INCREMENT PRIMARY KEY,
    category_id     INT          NOT NULL,
    assignment_name VARCHAR(100) NOT NULL,
    max_points      DECIMAL(6,2) NOT NULL DEFAULT 100,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- Students
CREATE TABLE Student (
    student_id     INT          AUTO_INCREMENT PRIMARY KEY,
    first_name     VARCHAR(50)  NOT NULL,
    last_name      VARCHAR(50)  NOT NULL,
    email          VARCHAR(100) UNIQUE
);

-- Enrollment: which students are in which course
CREATE TABLE Enrollment (
    enrollment_id  INT  AUTO_INCREMENT PRIMARY KEY,
    student_id     INT  NOT NULL,
    course_id      INT  NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id)  REFERENCES Course(course_id),
    UNIQUE (student_id, course_id)
);

-- Student scores on individual assignments
CREATE TABLE Submission (
    submission_id   INT           AUTO_INCREMENT PRIMARY KEY,
    student_id      INT           NOT NULL,
    assignment_id   INT           NOT NULL,
    score           DECIMAL(6,2),            -- NULL = not yet submitted
    FOREIGN KEY (student_id)    REFERENCES Student(student_id),
    FOREIGN KEY (assignment_id) REFERENCES Assignments(assignment_id),
    UNIQUE (student_id, assignment_id)
);


-- ============================================================
-- SAMPLE DATA (Task 3)
-- ============================================================

-- Professor
INSERT INTO Professor (first_name, last_name, email) VALUES
    ('Maria', 'Liu',    'mliu@university.edu');


-- Courses
INSERT INTO Course (professor_id, department, course_number, course_name, semester, year) VALUES
    (1, 'Computer Science', 'CS101', 'Introduction to Databases',   'Fall',   2024),
    (1, 'Computer Science', 'CS201', 'Data Structures',             'Spring', 2025);

-- Categories for CS101 (weights sum to 100)
INSERT INTO Category (course_id, category_name, weight_pct) VALUES
    (1, 'Participation', 10.00),
    (1, 'Homework',      20.00),
    (1, 'Tests',         50.00),
    (1, 'Projects',      20.00);

-- Categories for CS201 (weights sum to 100)
INSERT INTO Category (course_id, category_name, weight_pct) VALUES
    (2, 'Participation', 10.00),
    (2, 'Homework',      30.00),
    (2, 'Tests',         60.00);

-- Assignments for CS101
--   Participation (category_id=1)
INSERT INTO Assignments (category_id, assignment_name, max_points) VALUES
    (1, 'Week 1 Participation',  10),
    (1, 'Week 2 Participation',  10);
--   Homework (category_id=2) — 5 homeworks, each worth 20%/5 = 4%
INSERT INTO Assignments (category_id, assignment_name, max_points) VALUES
    (2, 'Homework 1', 100),
    (2, 'Homework 2', 100),
    (2, 'Homework 3', 100),
    (2, 'Homework 4', 100),
    (2, 'Homework 5', 100);
--   Tests (category_id=3)
INSERT INTO Assignments (category_id, assignment_name, max_points) VALUES
    (3, 'Midterm Exam', 100),
    (3, 'Final Exam',   100);
--   Projects (category_id=4)
INSERT INTO Assignments  (category_id, assignment_name, max_points) VALUES
    (4, 'Database Design Project', 100);

-- Assignments for CS201
--   Participation (category_id=5)
INSERT INTO Assignments  (category_id, assignment_name, max_points) VALUES
    (5, 'Week 1 Participation', 10),
    (5, 'Week 2 Participation', 10);
--   Homework (category_id=6)
INSERT INTO Assignments  (category_id, assignment_name, max_points) VALUES
    (6, 'Homework 1', 100),
    (6, 'Homework 2', 100),
    (6, 'Homework 3', 100);
--   Tests (category_id=7)
INSERT INTO Assignments  (category_id, assignment_name, max_points) VALUES
    (7, 'Midterm Exam', 100),
    (7, 'Final Exam',   100);

-- Students (includes names with 'Q' for Task 10)
INSERT INTO Student (first_name, last_name, email) VALUES
    ('Alice',   'Johnson',  'alice.johnson@email.com'),
    ('Bob',     'Smith',    'bob.smith@email.com'),
    ('Carol',   'Quinones', 'carol.quinones@email.com'),  -- last name has Q
    ('David',   'Brown',    'david.brown@email.com'),
    ('Eva',     'Quinn',    'eva.quinn@email.com'),        -- last name has Q
    ('Frank',   'Lee',      'frank.lee@email.com'),
    ('Grace',   'Martinez', 'grace.martinez@email.com'),
    ('Henry',   'Qiu',      'henry.qiu@email.com');        -- last name has Q

-- Enrollment: all 8 students in CS101; students 1-5 in CS201
INSERT INTO Enrollment (student_id, course_id) VALUES
    (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
    (1,2),(2,2),(3,2),(4,2),(5,2);

-- Submissions for CS101 assignments
-- assignment_ids 1-10 belong to CS101
INSERT INTO Submission (student_id, assignment_id, score) VALUES
-- Week 1 Participation (max 10)
(1,1,9),(2,1,8),(3,1,10),(4,1,7),(5,1,9),(6,1,6),(7,1,8),(8,1,10),
-- Week 2 Participation (max 10)
(1,2,10),(2,2,7),(3,2,9),(4,2,8),(5,2,10),(6,2,7),(7,2,9),(8,2,8),
-- Homework 1
(1,3,92),(2,3,85),(3,3,78),(4,3,90),(5,3,88),(6,3,72),(7,3,95),(8,3,80),
-- Homework 2
(1,4,88),(2,4,79),(3,4,82),(4,4,91),(5,4,76),(6,4,68),(7,4,93),(8,4,85),
-- Homework 3
(1,5,95),(2,5,82),(3,5,88),(4,5,87),(5,5,91),(6,5,75),(7,5,90),(8,5,78),
-- Homework 4
(1,6,90),(2,6,88),(3,6,85),(4,6,92),(5,6,80),(6,6,70),(7,6,88),(8,6,83),
-- Homework 5
(1,7,85),(2,7,80),(3,7,90),(4,7,88),(5,7,77),(6,7,65),(7,7,92),(8,7,79),
-- Midterm Exam
(1,8,88),(2,8,76),(3,8,83),(4,8,91),(5,8,79),(6,8,65),(7,8,87),(8,8,74),
-- Final Exam
(1,9,92),(2,9,80),(3,9,85),(4,9,88),(5,9,83),(6,9,70),(7,9,91),(8,9,78),
-- Database Design Project
(1,10,95),(2,10,85),(3,10,90),(4,10,92),(5,10,88),(6,10,75),(7,10,93),(8,10,82);


-- ============================================================
-- TASK 4: Average / Highest / Lowest score of an assignment
-- ============================================================
-- Example: stats for Homework 1 (assignment_id = 3)
SELECT
    a.assignment_name,
    ROUND(AVG(s.score), 2)  AS avg_score,
    MAX(s.score)             AS highest_score,
    MIN(s.score)             AS lowest_score,
    COUNT(s.score)           AS num_submissions
FROM Submission s
JOIN Assignments  a ON s.assignment_id = a.assignment_id
WHERE a.assignment_id = 3;


-- ============================================================
-- TASK 5: List all students in a given course
-- ============================================================
-- Example: all students in CS101 (course_id = 1)
SELECT
    st.student_id,
    st.first_name,
    st.last_name,
    st.email
FROM Student st
JOIN Enrollment e ON st.student_id = e.student_id
WHERE e.course_id = 1
ORDER BY st.last_name, st.first_name;


-- ============================================================
-- TASK 6: List all students AND all their scores in a course
-- ============================================================
SELECT
    st.first_name,
    st.last_name,
    a.assignment_name,
    cat.category_name,
    sub.score,
    a.max_points
FROM Student st
JOIN Enrollment  e   ON st.student_id    = e.student_id
JOIN Category    cat ON e.course_id      = cat.course_id
JOIN Assignments   a   ON cat.category_id  = a.category_id
LEFT JOIN Submission sub ON st.student_id = sub.student_id
                        AND a.assignment_id = sub.assignment_id
WHERE e.course_id = 1
ORDER BY st.last_name, st.first_name, cat.category_name, a.assignment_name;


-- ============================================================
-- TASK 7: Add an Assignments to a course
-- ============================================================
-- Add 'Homework 6' to CS101 Homework category (category_id = 2)
INSERT INTO Assignments  (category_id, assignment_name, max_points)
VALUES (2, 'Homework 6', 100);

-- Then add scores for all enrolled students (example: after adding HW6)
-- You would INSERT into Submission for each student.
-- Example for one student:
-- INSERT INTO Submission (student_id, assignment_id, score) VALUES (1, <new_id>, 88);


-- ============================================================
-- TASK 8: Change the weight percentages of categories for a course
-- ============================================================
-- Example: update CS101 — shift 5% from Projects to Tests
UPDATE Category SET weight_pct = 55.00 WHERE course_id = 1 AND category_name = 'Tests';
UPDATE Category SET weight_pct = 15.00 WHERE course_id = 1 AND category_name = 'Projects';
-- Verify they still sum to 100:
SELECT course_id, SUM(weight_pct) AS total_weight FROM Category WHERE course_id = 1;


-- ============================================================
-- TASK 9: Add 2 points to every student's score on one assignment
-- ============================================================
-- Example: add 2 pts to Midterm Exam (assignment_id = 8), cap at max_points
UPDATE Submission s
JOIN Assignments  a ON s.assignment_id = a.assignment_id
SET s.score = LEAST(s.score + 2, a.max_points)
WHERE s.assignment_id = 8;


-- ============================================================
-- TASK 10: Add 2 points ONLY to students whose last name contains 'Q'
-- ============================================================
UPDATE Submission s
JOIN Student st   ON s.student_id    = st.student_id
JOIN Assignments  a ON s.assignment_id = a.assignment_id
SET s.score = LEAST(s.score + 2, a.max_points)
WHERE s.assignment_id = 8
  AND st.last_name LIKE '%Q%';


-- ============================================================
-- TASK 11: Compute the final grade for a student
-- ============================================================
-- Formula:
--   For each category: student's avg score / max_points * category weight
--   Sum across all categories = final grade (out of 100)
--
-- Example: grade for student_id = 1 in course_id = 1

SELECT
    st.first_name,
    st.last_name,
    c.course_name,
    ROUND(SUM(cat_grade), 2) AS final_grade
FROM (
    SELECT
        sub.student_id,
        a.category_id,
        -- avg % score in this category × category weight
        (AVG(sub.score / a.max_points) * cat.weight_pct) AS cat_grade
    FROM Submission sub
    JOIN Assignments   a   ON sub.assignment_id = a.assignment_id
    JOIN Category    cat ON a.category_id     = cat.category_id
    WHERE cat.course_id = 1
      AND sub.student_id = 1
    GROUP BY sub.student_id, a.category_id, cat.weight_pct
) AS graded
JOIN Student st ON graded.student_id = st.student_id
JOIN Course  c  ON c.course_id = 1
GROUP BY st.student_id, st.first_name, st.last_name, c.course_name;


-- ============================================================
-- TASK 12: Grade for a student, dropping the lowest score per category
-- ============================================================
-- Strategy: rank each score lowest-to-highest within student+category using
-- ROW_NUMBER(). Drop rank=1 (the lowest) only when the category has more than
-- one graded submission; if there is only one submission keep it.

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
        WHERE cat.course_id = 1
          AND sub.student_id = 1
          AND sub.score IS NOT NULL
    ) AS ranked
    JOIN Category cat ON ranked.category_id = cat.category_id
    WHERE ranked.rn > 1 OR ranked.total_in_cat = 1
    GROUP BY ranked.student_id, ranked.category_id, cat.weight_pct
) AS graded
JOIN Student st ON graded.student_id = st.student_id
JOIN Course  c  ON c.course_id = 1
GROUP BY st.student_id, st.first_name, st.last_name, c.course_name;
