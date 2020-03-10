#184. Department Highest Salary
# Write your MySQL query statement below
select d.Department as Department,d.Name as Employee,d.Salary as Salary from (select c.Salary as Salary,c.Name as Name,c.DepartmentId as DepartmentId,b.Name as Department from Department b left join Employee c ON c.DepartmentId=b.Id) d,(select DepartmentId,max(Salary) as maxSalary from (select * from Employee Order by DepartmentId,Salary DESC) a group by a.DepartmentId) main where d.Salary=main.maxSalary and d.DepartmentId=main.DepartmentId
#Runtime: 1360 ms, faster than 7.13% of MySQL online submissions for Department Highest Salary.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.