# Write your MySQL query statement below
Select
    p.Product_id,
    ifnull(Round(Sum(p.price*u.units)/Sum(u.units),2),0) as average_price
From prices as p
Left join UnitsSold as u
on p.product_id = u.product_id
and u.purchase_date BETWEEN p.start_date and p.end_date
Group by product_id