# Write your MySQL query statement below
SELECT Employee.name as name, Bonus.bonus as bonus
FROM Employee LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
HAVING bonus < 1000 OR bonus is null