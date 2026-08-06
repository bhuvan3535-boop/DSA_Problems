# Write your MySQL query statement below
Select
    r.contest_id,
    Round((Count(r.user_id)/(Select count(*) from users)) * 100, 2) as percentage
From Register as r
Left Join users as u
on r.user_id = u.user_id
Group by r.contest_id
order by Round((Count(r.user_id)/(Select count(*) from users)) * 100, 2) Desc, contest_id Asc;