/*
Enter your query here.
*/
SELECT 
    con.contest_id,
    con.hacker_id,
    con.name,
    COALESCE(SUM(sagg.total_submissions), 0)             AS total_submissions,
    COALESCE(SUM(sagg.total_accepted_submissions), 0)    AS total_accepted_submissions,
    COALESCE(SUM(vagg.total_views), 0)                   AS total_views,
    COALESCE(SUM(vagg.total_unique_views), 0)            AS total_unique_views
FROM Contests con
JOIN Colleges col
  ON con.contest_id = col.contest_id
JOIN Challenges ch
  ON col.college_id = ch.college_id
LEFT JOIN (
    SELECT challenge_id,
           SUM(total_submissions)                    AS total_submissions,
           SUM(total_accepted_submissions)           AS total_accepted_submissions
    FROM Submission_Stats
    GROUP BY challenge_id
) sagg ON ch.challenge_id = sagg.challenge_id
LEFT JOIN (
    SELECT challenge_id,
           SUM(total_views)                         AS total_views,
           SUM(total_unique_views)                  AS total_unique_views
    FROM View_Stats
    GROUP BY challenge_id
) vagg ON ch.challenge_id = vagg.challenge_id
GROUP BY con.contest_id, con.hacker_id, con.name
HAVING 
    COALESCE(SUM(sagg.total_submissions), 0) +
    COALESCE(SUM(sagg.total_accepted_submissions), 0) +
    COALESCE(SUM(vagg.total_views), 0) +
    COALESCE(SUM(vagg.total_unique_views), 0) > 0
ORDER BY con.contest_id;
