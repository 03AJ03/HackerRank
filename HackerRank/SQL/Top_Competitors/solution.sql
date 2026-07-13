/*
Enter your query here.
*/
SELECT h.hacker_id, h.name
FROM hackers h
JOIN submissions s ON h.hacker_id = s.hacker_id
JOIN challenges c ON s.challenge_id = c.challenge_id
JOIN difficulty d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score             
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1    
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id ASC;
