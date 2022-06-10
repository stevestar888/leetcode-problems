# https://leetcode.com/problems/find-total-time-spent-by-each-employee/
select event_day as 'day', emp_id, SUM(out_time - in_time) AS 'total_time'
from Employees
group by day, emp_id
