-- 1068 Product Sales Analysis I
-- Problem Link: https://leetcode.com/problems/product-sales-analysis-i

SELECT
    p.product_name,
    s.year,
    s.price
FROM
    sales AS s
INNER JOIN
    product AS p
    ON s.product_id = p.product_id
ORDER BY
    s.year;