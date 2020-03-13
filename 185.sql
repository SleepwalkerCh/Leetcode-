185. Department Top Three Salaries
# Write your MySQL query statement below
    
select b.Name as Department,c.Name as Employee,c.Salary as Salary from Employee c join Department b ON c.DepartmentId=b.Id  where 3>(select count(distinct(d.salary)) from Employee d where c.DepartmentId=d.DepartmentId and d.Salary>c.Salary)
#Runtime: 804 ms, faster than 69.77% of MySQL online submissions for Department Top Three Salaries.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Top Three Salaries.