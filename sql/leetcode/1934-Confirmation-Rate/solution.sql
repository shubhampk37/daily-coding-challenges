-- 1934. Confirmation Rate
-- Problem Link: https://leetcode.com/problems/confirmation-rate

SELECT
    s.user_id,
    COALESCE(
        ROUND(
            SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) * 1.0
            / NULLIF(COUNT(c.action), 0),
        2),
    0.00) AS confirmation_rate
FROM 
    Signups AS s
LEFT JOIN
    Confirmations AS c
    ON s.user_id = c.user_id
GROUP BY
    s.user_id