/*
Enter your query here.
*/
WITH RECURSIVE Numbers(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1
    FROM Numbers
    WHERE n < 20  -- Number of rows P(20)
)
SELECT REPEAT('* ', n) AS Pattern
FROM Numbers
ORDER BY n;
