# Write your MySQL query statement below
SELECT
  round(COUNT(DISTINCT player_id) / (Select COUNT(DISTINCT player_id) from Activity), 2) as fraction
FROM
  Activity
WHERE
    (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
    IN(Select player_id, MIN(event_date) as first_login From Activity Group by player_id)