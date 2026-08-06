# Write your MySQL query statement below
Select 
    a.Machine_id as machine_id,
    round(avg(B.timestamp - A.timestamp), 3) as Processing_time
from Activity as A
JOIN
Activity as B
on a.machine_id = b.machine_id and a.process_id = b.process_id
and a.activity_type = 'Start' and b.activity_type = 'end'
group by a.machine_id;