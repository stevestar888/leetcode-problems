# https://leetcode.com/problems/customers-who-never-order/
select Customers.name AS 'Customers'
from Customers
left join Orders
on Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL

# select Customers.name AS 'Customers' from Customers
# WHERE id not in
# (select customerId from Orders)# SELECT Customers.name AS 'Customers' from Customers
# where Customers.id NOT IN
# (select customerId from Orders)