/*
Enter your query here.
*/
-- Query 1: Names alphabetically with first letter of occupation
SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')') AS NameWithOccupation
FROM OCCUPATIONS
ORDER BY Name ASC;

-- Query 2: Count of each occupation with required formatting
SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.') AS OccupationCount
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*) ASC, Occupation ASC;
