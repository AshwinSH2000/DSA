-- Write your PostgreSQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e, Department d 
WHERE e.departmentId = d.id
AND (e.departmentId, e.Salary) IN (
    SELECT employee.departmentId, MAX(employee.salary)
    FROM Employee
    GROUP BY employee.departmentId
)
