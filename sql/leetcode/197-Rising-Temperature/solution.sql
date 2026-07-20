-- 197. Rising Temperature
-- Problem Link: https://leetcode.com/problems/rising-temperature

-- Method 1(Faster):

-- w1: current day
-- w2: previous day
SELECT
    w1.id
FROM 
    weather AS w1
INNER JOIN 
    weather AS w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE
    w1.temperature > w2.temperature


/* --------------------------------- */

-- Method 2:
-- Was solved by sub-queries too, but for running the sub-query every time, the code will take longer to process and execute
-- a missing day can cause an issue, becuase we are asked COMPARISON STRICTLY WITH THE PREVIOUS DAY ONLY

