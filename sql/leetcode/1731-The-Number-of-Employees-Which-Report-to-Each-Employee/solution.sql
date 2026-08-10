-- LeetCode: 1731. The Number of Employees Which Report to Each Employee
-- Problem Link: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee

SELECT 
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM 
    Employees m
INNER JOIN 
    Employees e 
    ON m.employee_id = e.reports_to
GROUP BY 
    m.employee_id, 
    m.name
ORDER BY 
    m.employee_id;