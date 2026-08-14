-- LeetCode: 1789. Primary Department for Each Employee
-- Problem Link: https://leetcode.com/problems/primary-department-for-each-employee

-- Optimized code using Window Functions
-- Much faster
-- each employee's total department count in a single pass without needing a UNION

SELECT
    employee_id,
    department_id
FROM 
    (
        SELECT
            employee_id,
            department_id,
            primary_flag,
            COUNT(*) OVER (PARTITION BY employee_id) AS total_depts
        FROM
            Employee
    ) AS EmployeeDepartmentsCount
WHERE
    primary_flag = 'Y'
    OR total_depts = 1;



-- Previous Solution: UNION can degrade performance on larger datasets

-- SELECT
--     employee_id,
--     department_id
-- FROM
--     Employee
-- WHERE
--     primary_flag = 'Y'

-- UNION

-- SELECT
--     employee_id,
--     department_id
-- FROM
--     Employee
-- GROUP BY
--     employee_id
-- HAVING
--     COUNT(department_id) = 1;