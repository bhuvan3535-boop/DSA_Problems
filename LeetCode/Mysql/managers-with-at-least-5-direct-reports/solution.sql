Select 
    e1.name
From Employee as e1
Join(
    Select
        name,
        managerid,
        Count(*) as reports
    From Employee
    group by managerid
) e2
on e1.id = e2.managerid
Where reports >= 5