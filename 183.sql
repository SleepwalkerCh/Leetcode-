select Customers.Name as Customers from Customers left Join Orders on Orders.CustomerId=Customers.Id where Orders.Id is Null
#Runtime: 742 ms, faster than 26.41% of MySQL online submissions for Customers Who Never Order.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.