# LeetCode 1757: Recyclable and Low Fat Products

## Problem Link
[LeetCode 1757 - Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/)

## Problem Description
We are given a database table `Products` containing details about product features. The goal is to write a query to find the IDs of all products that are both low-fat (`low_fats = 'Y'`) and recyclable (`recyclable = 'Y'`).

## Approach
This is a straightforward selective query. We apply two filtering conditions in our `WHERE` clause using the logical `AND` operator to ensure both columns match our criteria.

## Query
```sql
SELECT product_id 
FROM Products 
WHERE low_fats = 'Y' 
  AND recyclable = 'Y';
```