# https://leetcode.com/problems/customers-who-never-order/

# There are two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

SELECT Name As Customers from Customers LEFT JOIN Orders on Customers.Id = Orders.CustomerId WHERE Orders.Id is null;