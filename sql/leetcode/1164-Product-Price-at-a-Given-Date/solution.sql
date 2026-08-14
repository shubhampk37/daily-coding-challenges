-- LeetCode: 1164. Product Price at a Given Date
-- Problem Link: https://leetcode.com/problems/product-price-at-a-given-date

WITH RankedProducts AS (
    SELECT
        product_id,
        new_price,
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
),

LatestPrices AS (
    SELECT
        product_id,
        new_price
    FROM
        RankedProducts
    WHERE
        rnk = 1
)

SELECT
    p.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM
    (   
        SELECT DISTINCT
            product_id
        FROM 
            Products
    ) AS p
LEFT JOIN 
    LatestPrices AS lp
    ON p.product_id = lp.product_id;