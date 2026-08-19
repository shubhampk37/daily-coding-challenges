-- LeetCode: 1341. Movie Rating
-- Problem Link: https://leetcode.com/problems/movie-rating

WITH MovieDetailRating AS (
    SELECT
        mr.movie_id,
        m.title,
        mr.user_id,
        mr.rating,
        mr.created_at
    FROM
        Movies AS m
    INNER JOIN
        MovieRating AS mr
        ON m.movie_id = mr.movie_id
)

(   
    -- Find the user with the greatest number of movie ratings
    SELECT
        u.name AS results
    FROM
        MovieDetailRating AS md
    INNER JOIN
        Users AS u
        ON md.user_id = u.user_id
    GROUP BY
        u.user_id,
        u.name
    ORDER BY
        COUNT(md.rating) DESC,
        u.name ASC
    LIMIT 1
)

UNION ALL

(
    -- Find the movie with the highest average rating in February 2020
    SELECT
        title AS results
    FROM
        MovieDetailRating
    WHERE
        DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
    GROUP BY
        movie_id,
        title
    ORDER BY
        AVG(rating) DESC,
        title ASC
    LIMIT 1
);
