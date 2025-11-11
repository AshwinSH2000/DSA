# Write your MySQL query statement below
# if you use group by, its condition need to be specified using HAVING
SELECT email AS Email
FROM Person
GROUP BY email
HAVING count(*) > 1