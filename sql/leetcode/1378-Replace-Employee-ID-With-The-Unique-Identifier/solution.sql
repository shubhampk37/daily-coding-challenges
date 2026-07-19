-- 1378 Replace Employee ID With The Unique Identifier
-- Problem Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

SELECT
    eui.unique_id,
    e.name
FROM
    employees AS e
LEFT JOIN
    employeeUNI AS eui
    ON e.id = eui.id;