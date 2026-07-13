/*
Enter your query here.
*/
WITH daily_submissions AS (
    SELECT
        submission_date,
        hacker_id,
        COUNT(*) AS submission_count
    FROM Submissions
    GROUP BY submission_date, hacker_id
),
top_hacker AS (
    SELECT
        submission_date,
        hacker_id,
        ROW_NUMBER() OVER (
            PARTITION BY submission_date
            ORDER BY submission_count DESC, hacker_id
        ) AS rn
    FROM daily_submissions
)

SELECT
    d.submission_date,
    (
        SELECT COUNT(*)
        FROM (
            SELECT hacker_id
            FROM Submissions s
            WHERE s.submission_date <= d.submission_date
            GROUP BY hacker_id
            HAVING COUNT(DISTINCT submission_date) =
                   DATEDIFF(
                       d.submission_date,
                       (SELECT MIN(submission_date) FROM Submissions)
                   ) + 1
        ) x
    ) AS total_hackers,
    t.hacker_id,
    h.name
FROM (
    SELECT DISTINCT submission_date
    FROM Submissions
) d
JOIN top_hacker t
    ON d.submission_date = t.submission_date
   AND t.rn = 1
JOIN Hackers h
    ON t.hacker_id = h.hacker_id
ORDER BY d.submission_date;
