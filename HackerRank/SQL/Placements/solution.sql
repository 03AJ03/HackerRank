/*
Enter your query here.
*/
SELECT s.name
FROM Students s
JOIN Friends f ON s.id = f.id
JOIN Packages ps ON s.id = ps.id
JOIN Packages pf ON f.friend_id = pf.id
WHERE pf.salary > ps.salary
ORDER BY pf.salary;
