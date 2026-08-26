-- LeetCode: 196. Delete Duplicate Emails
-- Problem Link: https://leetcode.com/problems/delete-duplicate-emails


DELETE
    p2
FROM
    Person AS p1
INNER JOIN
    Person AS p2
    ON p1.email = p2.email
    AND p1.id < p2.id;