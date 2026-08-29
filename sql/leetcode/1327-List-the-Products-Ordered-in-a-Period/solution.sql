-- LeetCode: 1327. List the Products Ordered in a Period
-- Problem Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period


WITH ProductQuantity AS (
    SELECT
        product_id,
        DATE_FORMAT(order_date, '%Y-%m') AS `year_month`,
        SUM(unit) AS unit
    FROM
        Orders
    WHERE 
        (order_date >= '2020-02-01' AND order_date < '2020-03-01')
    GROUP BY
        product_id,
        `year_month`
    HAVING 
        SUM(unit) >= 100
)

SELECT
    p.product_name,
    pq.unit
FROM
    ProductQuantity AS pq
INNER JOIN
    Products AS p
    ON pq.product_id = p.product_id
ORDER BY
    pq.unit DESC;