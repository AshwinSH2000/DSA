-- Write your PostgreSQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e JOIN Department d 
ON e.departmentId = d.id
WHERE (e.departmentId, e.Salary) IN (
    SELECT employee.departmentId, MAX(employee.salary)
    FROM Employee
    GROUP BY employee.departmentId
)
