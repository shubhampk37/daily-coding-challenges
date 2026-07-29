-- LeetCode: 1633. Percentage of Users Attended a Contest
-- Problem Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest

SELECT
    contest_id,
    ROUND(
        COUNT(user_id) * 100.0 / (
            SELECT 
                COUNT(*) 
            FROM Users
        ),
        2
    ) AS percentage
FROM
    register
GROUP BY
    contest_id
ORDER BY
    percentage DESC,
    contest_id ASC;