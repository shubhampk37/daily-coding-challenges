-- LeetCode: 1204. Last Person to Fit in the Bus
-- Problem Link: https://leetcode.com/problems/last-person-to-fit-in-the-bus

WITH RunningTotal  AS (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn ASC) AS cumulative_weight
    FROM
        Queue
)

SELECT
    person_name
FROM
    RunningTotal
WHERE
    cumulative_weight <= 1000
ORDER BY 
    cumulative_weight DESC
LIMIT 1;