-- LeetCode: 1321. Restaurant Growth
-- Problem Link: https://leetcode.com/problems/restaurant-growth



WITH DailyAmountCollection AS (
    -- Step 1: Aggregate total amount per day
    SELECT
    visited_on,
    SUM(amount) AS amount
    FROM
        Customer
    GROUP BY
        visited_on
),

WindowSummary AS (
    -- Step: compute 7 day rolling sum and average
    SELECT
        visited_on,
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(
            AVG(amount) OVER (
                ORDER BY visited_on
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ), 2
        ) AS average_amount,
        ROW_NUMBER() OVER (
            ORDER BY visited_on
        ) AS row_num
    FROM
        DailyAmountCollection
)

-- Show the total amount and average_amount for days which have the window of 6 days prior to that date
SELECT
    visited_on,
    amount,
    average_amount 
FROM 
    WindowSummary
WHERE 
    row_num >= 7
ORDER BY
    visited_on ASC;
