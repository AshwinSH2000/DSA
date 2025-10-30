# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE ( area >= 3e6 || population >= 25e6 )