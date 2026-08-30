-- LeetCode: 1517. Find Users With Valid E-Mails
-- Problem Link: https://leetcode.com/problems/find-users-with-valid-e-mails


SELECT
    user_id,
    name,
    mail
FROM 
    Users
WHERE
    REGEXP_LIKE(
        mail,
        '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$', 
        'c' -- 'c' flag enforces case-sensitivity
    );