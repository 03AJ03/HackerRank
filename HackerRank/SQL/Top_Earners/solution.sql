/*
Enter your query here.
*/
SELECT MAX(salary*months), COUNT(*)
FROM Employee
WHERE Salary*months=(SELECT MAX(SALARY * MONTHS) FROM EMPLOYEE);
