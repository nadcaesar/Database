---
[```
    +----------------------------------+
    |                                  |
    +----------------------------------+
    | TASK 4 ÔÇö Assignment Statistics |
    +----------------------------------+
    1 row in set (0.004 sec)

    +-------------------------+-----------+---------------+--------------+-----------------+
    | assignment_name         | avg_score | highest_score | lowest_score | num_submissions |
    +-------------------------+-----------+---------------+--------------+-----------------+
    | Week 1 Participation    |      8.38 |         10.00 |         6.00 |               8 |
    | Week 2 Participation    |      8.50 |         10.00 |         7.00 |               8 |
    | Homework 1              |     85.00 |         95.00 |        72.00 |               8 |
    | Homework 2              |     82.75 |         93.00 |        68.00 |               8 |
    | Homework 3              |     85.75 |         95.00 |        75.00 |               8 |
    | Homework 4              |     84.50 |         92.00 |        70.00 |               8 |
    | Homework 5              |     82.00 |         92.00 |        65.00 |               8 |
    | Midterm Exam            |     83.13 |         93.00 |        67.00 |               8 |
    | Final Exam              |     83.38 |         92.00 |        70.00 |               8 |
    | Database Design Project |     87.50 |         95.00 |        75.00 |               8 |
    +-------------------------+-----------+---------------+--------------+-----------------+
    10 rows in set (0.007 sec)

    Query OK, 0 rows affected (0.004 sec)

    Query OK, 0 rows affected (0.002 sec)

    Query OK, 0 rows affected (0.002 sec)

    +----------------------------------------------+
    |                                              |
    +----------------------------------------------+
    | TASK 5 ÔÇö Students in CS101 (course_id = 1) |
    +----------------------------------------------+
    1 row in set (0.003 sec)

    +------------+------------+-----------+--------------------------+
    | student_id | first_name | last_name | email                    |
    +------------+------------+-----------+--------------------------+
    |          4 | David      | Brown     | david.brown@email.com    |
    |          1 | Alice      | Johnson   | alice.johnson@email.com  |
    |          6 | Frank      | Lee       | frank.lee@email.com      |
    |          7 | Grace      | Martinez  | grace.martinez@email.com |
    |          8 | Henry      | Qiu       | henry.qiu@email.com      |
    |          5 | Eva        | Quinn     | eva.quinn@email.com      |
    |          3 | Carol      | Quinones  | carol.quinones@email.com |
    |          2 | Bob        | Smith     | bob.smith@email.com      |
    +------------+------------+-----------+--------------------------+
    8 rows in set (0.009 sec)

    +----------------------------------------------+
    |                                              |
    +----------------------------------------------+
    | TASK 5 ÔÇö Students in CS201 (course_id = 2) |
    +----------------------------------------------+
    1 row in set (0.004 sec)

    +------------+------------+-----------+--------------------------+
    | student_id | first_name | last_name | email                    |
    +------------+------------+-----------+--------------------------+
    |          4 | David      | Brown     | david.brown@email.com    |
    |          1 | Alice      | Johnson   | alice.johnson@email.com  |
    |          5 | Eva        | Quinn     | eva.quinn@email.com      |
    |          3 | Carol      | Quinones  | carol.quinones@email.com |
    |          2 | Bob        | Smith     | bob.smith@email.com      |
    +------------+------------+-----------+--------------------------+
    5 rows in set (0.009 sec)

    Query OK, 0 rows affected (0.004 sec)

    Query OK, 0 rows affected (0.002 sec)

    Query OK, 0 rows affected (0.003 sec)

    +-------------------------------------------------------------+
    |                                                             |
    +-------------------------------------------------------------+
    | TASK 6 ÔÇö All Students and Scores in CS101 (course_id = 1) |
    +-------------------------------------------------------------+
    1 row in set (0.004 sec)

    +------------+-----------+---------------+-------------------------+-------+------------+
    | first_name | last_name | category_name | assignment_name         | score | max_points |
    +------------+-----------+---------------+-------------------------+-------+------------+
    | David      | Brown     | Homework      | Homework 1              | 90.00 |     100.00 |
    | David      | Brown     | Homework      | Homework 2              | 91.00 |     100.00 |
    | David      | Brown     | Homework      | Homework 3              | 87.00 |     100.00 |
    | David      | Brown     | Homework      | Homework 4              | 92.00 |     100.00 |
    | David      | Brown     | Homework      | Homework 5              | 88.00 |     100.00 |
    | David      | Brown     | Homework      | Homework 6              |  NULL |     100.00 |
    | David      | Brown     | Participation | Week 1 Participation    |  7.00 |      10.00 |
    | David      | Brown     | Participation | Week 2 Participation    |  8.00 |      10.00 |
    | David      | Brown     | Projects      | Database Design Project | 92.00 |     100.00 |
    | David      | Brown     | Tests         | Final Exam              | 88.00 |     100.00 |
    | David      | Brown     | Tests         | Midterm Exam            | 93.00 |     100.00 |
    | Alice      | Johnson   | Homework      | Homework 1              | 92.00 |     100.00 |
    | Alice      | Johnson   | Homework      | Homework 2              | 88.00 |     100.00 |
    | Alice      | Johnson   | Homework      | Homework 3              | 95.00 |     100.00 |
    | Alice      | Johnson   | Homework      | Homework 4              | 90.00 |     100.00 |
    | Alice      | Johnson   | Homework      | Homework 5              | 85.00 |     100.00 |
    | Alice      | Johnson   | Homework      | Homework 6              |  NULL |     100.00 |
    | Alice      | Johnson   | Participation | Week 1 Participation    |  9.00 |      10.00 |
    | Alice      | Johnson   | Participation | Week 2 Participation    | 10.00 |      10.00 |
    | Alice      | Johnson   | Projects      | Database Design Project | 95.00 |     100.00 |
    | Alice      | Johnson   | Tests         | Final Exam              | 92.00 |     100.00 |
    | Alice      | Johnson   | Tests         | Midterm Exam            | 90.00 |     100.00 |
    | Frank      | Lee       | Homework      | Homework 1              | 72.00 |     100.00 |
    | Frank      | Lee       | Homework      | Homework 2              | 68.00 |     100.00 |
    | Frank      | Lee       | Homework      | Homework 3              | 75.00 |     100.00 |
    | Frank      | Lee       | Homework      | Homework 4              | 70.00 |     100.00 |
    | Frank      | Lee       | Homework      | Homework 5              | 65.00 |     100.00 |
    | Frank      | Lee       | Homework      | Homework 6              |  NULL |     100.00 |
    | Frank      | Lee       | Participation | Week 1 Participation    |  6.00 |      10.00 |
    | Frank      | Lee       | Participation | Week 2 Participation    |  7.00 |      10.00 |
    | Frank      | Lee       | Projects      | Database Design Project | 75.00 |     100.00 |
    | Frank      | Lee       | Tests         | Final Exam              | 70.00 |     100.00 |
    | Frank      | Lee       | Tests         | Midterm Exam            | 67.00 |     100.00 |
    | Grace      | Martinez  | Homework      | Homework 1              | 95.00 |     100.00 |
    | Grace      | Martinez  | Homework      | Homework 2              | 93.00 |     100.00 |
    | Grace      | Martinez  | Homework      | Homework 3              | 90.00 |     100.00 |
    | Grace      | Martinez  | Homework      | Homework 4              | 88.00 |     100.00 |
    | Grace      | Martinez  | Homework      | Homework 5              | 92.00 |     100.00 |
    | Grace      | Martinez  | Homework      | Homework 6              |  NULL |     100.00 |
    | Grace      | Martinez  | Participation | Week 1 Participation    |  8.00 |      10.00 |
    | Grace      | Martinez  | Participation | Week 2 Participation    |  9.00 |      10.00 |
    | Grace      | Martinez  | Projects      | Database Design Project | 93.00 |     100.00 |
    | Grace      | Martinez  | Tests         | Final Exam              | 91.00 |     100.00 |
    | Grace      | Martinez  | Tests         | Midterm Exam            | 89.00 |     100.00 |
    | Henry      | Qiu       | Homework      | Homework 1              | 80.00 |     100.00 |
    | Henry      | Qiu       | Homework      | Homework 2              | 85.00 |     100.00 |
    | Henry      | Qiu       | Homework      | Homework 3              | 78.00 |     100.00 |
    | Henry      | Qiu       | Homework      | Homework 4              | 83.00 |     100.00 |
    | Henry      | Qiu       | Homework      | Homework 5              | 79.00 |     100.00 |
    | Henry      | Qiu       | Homework      | Homework 6              |  NULL |     100.00 |
    | Henry      | Qiu       | Participation | Week 1 Participation    | 10.00 |      10.00 |
    | Henry      | Qiu       | Participation | Week 2 Participation    |  8.00 |      10.00 |
    | Henry      | Qiu       | Projects      | Database Design Project | 82.00 |     100.00 |
    | Henry      | Qiu       | Tests         | Final Exam              | 78.00 |     100.00 |
    | Henry      | Qiu       | Tests         | Midterm Exam            | 78.00 |     100.00 |
    | Eva        | Quinn     | Homework      | Homework 1              | 88.00 |     100.00 |
    | Eva        | Quinn     | Homework      | Homework 2              | 76.00 |     100.00 |
    | Eva        | Quinn     | Homework      | Homework 3              | 91.00 |     100.00 |
    | Eva        | Quinn     | Homework      | Homework 4              | 80.00 |     100.00 |
    | Eva        | Quinn     | Homework      | Homework 5              | 77.00 |     100.00 |
    | Eva        | Quinn     | Homework      | Homework 6              |  NULL |     100.00 |
    | Eva        | Quinn     | Participation | Week 1 Participation    |  9.00 |      10.00 |
    | Eva        | Quinn     | Participation | Week 2 Participation    | 10.00 |      10.00 |
    | Eva        | Quinn     | Projects      | Database Design Project | 88.00 |     100.00 |
    | Eva        | Quinn     | Tests         | Final Exam              | 83.00 |     100.00 |
    | Eva        | Quinn     | Tests         | Midterm Exam            | 83.00 |     100.00 |
    | Carol      | Quinones  | Homework      | Homework 1              | 78.00 |     100.00 |
    | Carol      | Quinones  | Homework      | Homework 2              | 82.00 |     100.00 |
    | Carol      | Quinones  | Homework      | Homework 3              | 88.00 |     100.00 |
    | Carol      | Quinones  | Homework      | Homework 4              | 85.00 |     100.00 |
    | Carol      | Quinones  | Homework      | Homework 5              | 90.00 |     100.00 |
    | Carol      | Quinones  | Homework      | Homework 6              |  NULL |     100.00 |
    | Carol      | Quinones  | Participation | Week 1 Participation    | 10.00 |      10.00 |
    | Carol      | Quinones  | Participation | Week 2 Participation    |  9.00 |      10.00 |
    | Carol      | Quinones  | Projects      | Database Design Project | 90.00 |     100.00 |
    | Carol      | Quinones  | Tests         | Final Exam              | 85.00 |     100.00 |
    | Carol      | Quinones  | Tests         | Midterm Exam            | 87.00 |     100.00 |
    | Bob        | Smith     | Homework      | Homework 1              | 85.00 |     100.00 |
    | Bob        | Smith     | Homework      | Homework 2              | 79.00 |     100.00 |
    | Bob        | Smith     | Homework      | Homework 3              | 82.00 |     100.00 |
    | Bob        | Smith     | Homework      | Homework 4              | 88.00 |     100.00 |
    | Bob        | Smith     | Homework      | Homework 5              | 80.00 |     100.00 |
    | Bob        | Smith     | Homework      | Homework 6              |  NULL |     100.00 |
    | Bob        | Smith     | Participation | Week 1 Participation    |  8.00 |      10.00 |
    | Bob        | Smith     | Participation | Week 2 Participation    |  7.00 |      10.00 |
    | Bob        | Smith     | Projects      | Database Design Project | 85.00 |     100.00 |
    | Bob        | Smith     | Tests         | Final Exam              | 80.00 |     100.00 |
    | Bob        | Smith     | Tests         | Midterm Exam            | 78.00 |     100.00 |
    +------------+-----------+---------------+-------------------------+-------+------------+
    88 rows in set (0.020 sec)

    Query OK, 0 rows affected (0.004 sec)

    Query OK, 0 rows affected (0.002 sec)

    Query OK, 0 rows affected (0.002 sec)

    +-----------------------------------------------------------+
    |                                                           |
    +-----------------------------------------------------------+
    | TASK 7 ÔÇö Before: Assignments in CS101 Homework category |
    +-----------------------------------------------------------+
    1 row in set (0.002 sec)

    +---------------+-----------------+------------+
    | assignment_id | assignment_name | max_points |
    +---------------+-----------------+------------+
    |             3 | Homework 1      |     100.00 |
    |             4 | Homework 2      |     100.00 |
    |             5 | Homework 3      |     100.00 |
    |             6 | Homework 4      |     100.00 |
    |             7 | Homework 5      |     100.00 |
    |            18 | Homework 6      |     100.00 |
    +---------------+-----------------+------------+
    6 rows in set (0.012 sec)

    Query OK, 1 row affected (0.049 sec)

    +------------------------------------+
    |                                    |
    +------------------------------------+
    | TASK 7 ÔÇö After: Homework 6 added |
    +------------------------------------+
    1 row in set (0.003 sec)

    +---------------+-----------------+------------+
    | assignment_id | assignment_name | max_points |
    +---------------+-----------------+------------+
    |             3 | Homework 1      |     100.00 |
    |             4 | Homework 2      |     100.00 |
    |             5 | Homework 3      |     100.00 |
    |             6 | Homework 4      |     100.00 |
    |             7 | Homework 5      |     100.00 |
    |            18 | Homework 6      |     100.00 |
    |            19 | Homework 6      |     100.00 |
    +---------------+-----------------+------------+
    7 rows in set (0.005 sec)

    Query OK, 0 rows affected (0.003 sec)

    Query OK, 0 rows affected (0.002 sec)

    Query OK, 0 rows affected (0.001 sec)

    +-----------------------------------------------+
    |                                               |
    +-----------------------------------------------+
    | TASK 8 ÔÇö Before: Category weights for CS101 |
    +-----------------------------------------------+
    1 row in set (0.003 sec)

    +---------------+------------+
    | category_name | weight_pct |
    +---------------+------------+
    | Homework      |      20.00 |
    | Participation |      10.00 |
    | Projects      |      15.00 |
    | Tests         |      55.00 |
    +---------------+------------+
    4 rows in set (0.004 sec)

    Query OK, 0 rows affected (0.007 sec)
    Rows matched: 1  Changed: 0  Warnings: 0

    Query OK, 0 rows affected (0.004 sec)
    Rows matched: 1  Changed: 0  Warnings: 0

    +-----------------------------------------------------------------+
    |                                                                 |
    +-----------------------------------------------------------------+
    | TASK 8 ÔÇö After: Updated weights (TestsÔåÆ55%, ProjectsÔåÆ15%) |
    +-----------------------------------------------------------------+
    1 row in set (0.003 sec)

    +---------------+------------+
    | category_name | weight_pct |
    +---------------+------------+
    | Homework      |      20.00 |
    | Participation |      10.00 |
    | Projects      |      15.00 |
    | Tests         |      55.00 |
    +---------------+------------+
    4 rows in set (0.005 sec)

    +--------------------------------------+
    |                                      |
    +--------------------------------------+
    | TASK 8 ÔÇö Verify weights sum to 100 |
    +--------------------------------------+
    1 row in set (0.002 sec)

    +-----------+--------------+
    | course_id | total_weight |
    +-----------+--------------+
    |         1 |       100.00 |
    +-----------+--------------+
    1 row in set (0.003 sec)

    Query OK, 0 rows affected (0.001 sec)

    Query OK, 0 rows affected (0.001 sec)

    Query OK, 0 rows affected (0.001 sec)

    +------------------------------------------------------------+
    |                                                            |
    +------------------------------------------------------------+
    | TASK 9 ÔÇö Before: Midterm Exam scores (assignment_id = 8) |
    +------------------------------------------------------------+
    1 row in set (0.001 sec)

    +------------+-----------+-------+
    | first_name | last_name | score |
    +------------+-----------+-------+
    | David      | Brown     | 93.00 |
    | Alice      | Johnson   | 90.00 |
    | Frank      | Lee       | 67.00 |
    | Grace      | Martinez  | 89.00 |
    | Henry      | Qiu       | 78.00 |
    | Eva        | Quinn     | 83.00 |
    | Carol      | Quinones  | 87.00 |
    | Bob        | Smith     | 78.00 |
    +------------+-----------+-------+
    8 rows in set (0.006 sec)

    Query OK, 8 rows affected (0.035 sec)
    Rows matched: 8  Changed: 8  Warnings: 0

    +---------------------------------------------------+
    |                                                   |
    +---------------------------------------------------+
    | TASK 9 ÔÇö After: +2 points added to all students |
    +---------------------------------------------------+
    1 row in set (0.002 sec)

    +------------+-----------+-------+
    | first_name | last_name | score |
    +------------+-----------+-------+
    | David      | Brown     | 95.00 |
    | Alice      | Johnson   | 92.00 |
    | Frank      | Lee       | 69.00 |
    | Grace      | Martinez  | 91.00 |
    | Henry      | Qiu       | 80.00 |
    | Eva        | Quinn     | 85.00 |
    | Carol      | Quinones  | 89.00 |
    | Bob        | Smith     | 80.00 |
    +------------+-----------+-------+
    8 rows in set (0.004 sec)

    Query OK, 0 rows affected (0.002 sec)

    Query OK, 0 rows affected (0.001 sec)

    Query OK, 0 rows affected (0.001 sec)

    +---------------------------------------------------------------+
    |                                                               |
    +---------------------------------------------------------------+
    | TASK 10 ÔÇö Before: Scores for students with 'Q' in last name |
    +---------------------------------------------------------------+
    1 row in set (0.001 sec)

    +------------+-----------+-------+
    | first_name | last_name | score |
    +------------+-----------+-------+
    | Henry      | Qiu       | 80.00 |
    | Eva        | Quinn     | 85.00 |
    | Carol      | Quinones  | 89.00 |
    +------------+-----------+-------+
    3 rows in set (0.007 sec)

    Query OK, 3 rows affected (0.035 sec)
    Rows matched: 3  Changed: 3  Warnings: 0

    +----------------------------------------------------+
    |                                                    |
    +----------------------------------------------------+
    | TASK 10 ÔÇö After: +2 points only for 'Q' students |
    +----------------------------------------------------+
    1 row in set (0.003 sec)

    +------------+-----------+-------+
    | first_name | last_name | score |
    +------------+-----------+-------+
    | David      | Brown     | 95.00 |
    | Alice      | Johnson   | 92.00 |
    | Frank      | Lee       | 69.00 |
    | Grace      | Martinez  | 91.00 |
    | Henry      | Qiu       | 82.00 |
    | Eva        | Quinn     | 87.00 |
    | Carol      | Quinones  | 91.00 |
    | Bob        | Smith     | 80.00 |
    +------------+-----------+-------+
    8 rows in set (0.004 sec)

    Query OK, 0 rows affected (0.003 sec)

    Query OK, 0 rows affected (0.002 sec)

    Query OK, 0 rows affected (0.002 sec)

    +---------------------------------------------------+
    |                                                   |
    +---------------------------------------------------+
    | TASK 11 ÔÇö Final Grade for All Students in CS101 |
    +---------------------------------------------------+
    1 row in set (0.004 sec)

    +------------+-----------+---------------------------+-------------+
    | first_name | last_name | course_name               | final_grade |
    +------------+-----------+---------------------------+-------------+
    | Alice      | Johnson   | Introduction to Databases |       92.35 |
    | Grace      | Martinez  | Introduction to Databases |       90.82 |
    | David      | Brown     | Introduction to Databases |       89.55 |
    | Carol      | Quinones  | Introduction to Databases |       88.32 |
    | Eva        | Quinn     | Introduction to Databases |       85.93 |
    | Henry      | Qiu       | Introduction to Databases |       81.50 |
    | Bob        | Smith     | Introduction to Databases |       80.81 |
    | Frank      | Lee       | Introduction to Databases |       69.98 |
    +------------+-----------+---------------------------+-------------+
    8 rows in set (0.023 sec)

    Query OK, 0 rows affected (0.006 sec)

    Query OK, 0 rows affected (0.004 sec)

    Query OK, 0 rows affected (0.002 sec)

    +------------------------------------------------------------------------------+
    |                                                                              |
    +------------------------------------------------------------------------------+
    | TASK 12 ÔÇö Final Grade (Drop Lowest per Category) for All Students in CS101 |
    +------------------------------------------------------------------------------+
    1 row in set (0.002 sec)

    +------------+-----------+---------------------------+-------------------------+
    | first_name | last_name | course_name               | final_grade_drop_lowest |
    +------------+-----------+---------------------------+-------------------------+
    | David      | Brown     | Introduction to Databases |                   78.30 |
    | Carol      | Quinones  | Introduction to Databases |                   77.30 |
    | Eva        | Quinn     | Introduction to Databases |                   74.65 |
    | Henry      | Qiu       | Introduction to Databases |                   71.45 |
    | Frank      | Lee       | Introduction to Databases |                   59.75 |
    | Alice      | Johnson   | Introduction to Databases |                   28.25 |
    | Grace      | Martinez  | Introduction to Databases |                   27.50 |
    | Bob        | Smith     | Introduction to Databases |                   24.75 |
    +------------+-----------+---------------------------+-------------------------+
    8 rows in set (0.034 sec)
```
]
---