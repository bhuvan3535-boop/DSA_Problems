# Write your MySQL query statement below
Select
    p.project_id,
    Round(Avg(e.experience_years), 2) as average_years
From project as p
Left Join Employee as e
on p.employee_id = e.employee_id
group by Project_id