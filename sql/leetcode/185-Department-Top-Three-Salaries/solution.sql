-- LeetCode: 185. Department Top Three Salaries
-- Problem Link: https://leetcode.com/problems/department-top-three-salaries



WITH RankedEmployees AS (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM
        Employee AS e
    JOIN
        Department AS d
        ON e.departmentId = d.id
)
SELECT 
    Department, 
    Employee,
    Salary
FROM
    RankedEmployees
WHERE
    salary_rank <= 3;