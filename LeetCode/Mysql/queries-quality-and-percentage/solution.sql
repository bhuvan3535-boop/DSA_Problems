# Write your MySQL query statement below
Select
    query_name,
    Round(Avg(rating/position),2) as quality,
    Round((Sum(case when rating < 3 then 1 else 0 end)/count(*))*100, 2) as poor_query_percentage 
From Queries
Group by query_name