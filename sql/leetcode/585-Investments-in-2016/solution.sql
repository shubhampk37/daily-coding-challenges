-- LeetCode: 585. Investments in 2016
-- Problem Link: https://leetcode.com/problems/investments-in-2016



SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT 
        tiv_2016,
        COUNT(*) OVER (
            PARTITION BY tiv_2015
        ) AS tiv_2015_count,
        COUNT(*) OVER (
            PARTITION BY lat, lon
        ) AS city_count
    FROM
        Insurance
) AS sub
WHERE
    -- tiv_2015 shared with 1 or more other policy holders
    tiv_2015_count > 1
    -- check if lat, lon i.e the cities are unique
    AND city_count = 1;