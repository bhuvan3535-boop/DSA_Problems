# Write your MySQL query statement below
Select
    e.name,
    b.bonus
From Employee as e
left join Bonus as b
on e.empid = b.empid
Where b.bonus < 1000 or
b.bonus is NULL;