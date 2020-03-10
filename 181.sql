#181. Employees Earning More Than Their Managers
# Write your MySQL query statement below
select A.Name as Employee from Employee A , Employee B where A.ManagerId=B.Id and A.Salary>B.Salary 
#Runtime: 304 ms, faster than 98.55% of MySQL online submissions for Employees Earning More Than Their Managers.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.