/*
Enter your query here.
*/
WITH RECURSIVE Numbers(n) AS (
    SELECT 2
    UNION ALL
    SELECT n + 1
    FROM Numbers
    WHERE n < 1000
),
Primes AS (
    SELECT n
    FROM Numbers num
    WHERE NOT EXISTS (
        SELECT 1
        FROM Numbers d
        WHERE d.n < num.n
          AND num.n % d.n = 0
          AND d.n > 1
    )
)
SELECT GROUP_CONCAT(n SEPARATOR '&') AS PrimeNumbers
FROM Primes;
