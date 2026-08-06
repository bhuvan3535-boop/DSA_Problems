# Write your MySQL query statement below
select
    product_id,
    year as first_year,
    quantity,
    price
from(
        select
            sale_id,
            product_id,
            year,
            rank() over(partition by product_id order by year asc) as r,
            quantity,
            price
        from sales)t
where r = 1;
