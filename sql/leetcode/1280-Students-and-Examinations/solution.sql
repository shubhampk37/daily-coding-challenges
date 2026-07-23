-- 1280. Students and Examinations
-- Problem Link: https://leetcode.com/problems/students-and-examinations

-- Students with all of their subjects
WITH StudentsSubjects AS(
    SELECT
        *
    FROM 
        Students AS s
    CROSS JOIN
        Subjects AS sub
)

-- Checking if the student has appeared for the xam or not, if yes, then how many attempts
SELECT
    s.student_id,
    s.student_name,
    s.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM
    StudentsSubjects AS s
LEFT JOIN
    Examinations AS e
    ON s.student_id = e.student_id
    AND s.subject_name = e.subject_name
GROUP BY
    s.student_id,
    s.student_name,
    s.subject_name
ORDER BY 
    s.student_id,
    s.subject_name;
