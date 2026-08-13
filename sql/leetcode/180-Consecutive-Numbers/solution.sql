-- LeetCode: 180. Consecutive Numbers
-- Problem Link: https://leetcode.com/problems/consecutive-numbers

SELECT DISTINCT 
    num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num,
        LEAD(num, 2) OVER (ORDER BY id) AS next_next_num
    FROM 
        Logs
) AS evaluated_logs
WHERE 
    num = next_num 
    AND num = next_next_num;