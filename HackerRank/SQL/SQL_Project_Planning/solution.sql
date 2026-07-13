/*
Enter your query here.
*/
SELECT MIN(Start_Date) AS Start_Date,
       MAX(End_Date) AS End_Date
FROM (
    SELECT 
        Start_Date,
        End_Date,
        DATE_SUB(Start_Date, INTERVAL ROW_NUMBER() OVER (ORDER BY Start_Date) DAY) AS grp
    FROM Projects
) AS t
GROUP BY grp
ORDER BY DATEDIFF(MAX(End_Date), MIN(Start_Date)), MIN(Start_Date);
