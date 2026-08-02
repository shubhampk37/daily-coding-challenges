-- LeetCode: 550. Game Play Analysis IV
-- Problem Link: https://leetcode.com/problems/game-play-analysis-iv

#INITIAL Logins
WITH FirstLogin AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM 
        Activity
    GROUP BY
        player_id
)

SELECT
    ROUND(
        COUNT(a.player_id) / COUNT(f.player_id),
        2
    ) AS fraction
FROM
    FirstLogin AS f
LEFT JOIN
    Activity AS a
    ON f.player_id = a.player_id
    # Check if the next login happens on the folowing day
    AND DATE_ADD(f.first_login, INTERVAL 1 DAY) = a.event_date

