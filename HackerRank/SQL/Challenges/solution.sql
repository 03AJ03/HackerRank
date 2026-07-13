/*
Enter your query here.
*/
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS total_challenges
FROM Hackers h
JOIN Challenges c 
  ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING 
    COUNT(c.challenge_id) = (
        SELECT MAX(challenge_count)
        FROM (
            SELECT COUNT(challenge_id) AS challenge_count
            FROM Challenges
            GROUP BY hacker_id
        ) AS t1
    )
    OR COUNT(c.challenge_id) IN (
        SELECT challenge_count
        FROM (
            SELECT challenge_count
            FROM (
                SELECT COUNT(challenge_id) AS challenge_count
                FROM Challenges
                GROUP BY hacker_id
            ) AS t2
            GROUP BY challenge_count
            HAVING COUNT(*) = 1
        ) AS unique_counts
    )
ORDER BY total_challenges DESC, h.hacker_id;
