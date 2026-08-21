-- LeetCode: 602. Friend Requests II Who Has the Most Friends
-- Problem Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends



WITH AllFriends AS (
    SELECT
        requester_id AS id
    FROM
        RequestAccepted
        
    UNION ALL

    SELECT
        accepter_id AS id
    FROM
        RequestAccepted
)

SELECT
    id,
    COUNT(*) AS num
FROM
    AllFriends
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1;