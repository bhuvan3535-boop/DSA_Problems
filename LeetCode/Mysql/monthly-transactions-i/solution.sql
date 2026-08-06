# Write your MySQL query statement below
Select
    Date_Format(trans_date, '%Y-%m') as month,
    country,
    Count(*) as trans_count,
    Count(case when state="approved" then amount else null end) as approved_count,
    Sum(Amount) as trans_total_amount,
    Sum(case when state="approved" then amount else 0 end) as approved_total_amount
From Transactions
Group by Date_Format(trans_date, '%Y-%m'), country;