-- 570. Managers with at Least 5 Direct Reports
-- Problem Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports

-- Find the names of the managers who have at least 5 direct reports
SELECT
    name
FROM
    Employee
WHERE
    id IN (
        -- Find `managerId`s that appear 5 or more times
        SELECT
            managerId
        FROM
            Employee
        GROUP BY
            managerId
        HAVING
            COUNT(id) >= 5
    );