# Write your MySQL query statement below
SELECT s.user_id, ROUND(IFNULL(c.confirmation_count/t.total_count,0),2) as confirmation_rate
FROM Signups s
LEFT JOIN (SELECT user_id, count(*) as total_count
from confirmations
GROUP by user_id) as t on s.user_id = t.user_id
LEFT JOIN (SELECT user_id, count(*) as confirmation_count
FROM Confirmations
WHERE action = 'confirmed'
GROUP BY user_id) as c on s.user_id = c.user_id