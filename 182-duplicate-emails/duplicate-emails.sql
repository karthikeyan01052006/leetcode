# Write your MySQL query statement below
SELECT email AS Email
FROM person
GROUP BY Email
having COUNT(email) > 1;