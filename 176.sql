# 176. Second Highest Salary
# Write your MySQL query statement below
select max(e1.Salary) as SecondHighestSalary from Employee e1,(select max(Salary) as Salary from Employee) e2 where e1.Salary<e2.Salary
#Runtime: 140 ms, faster than 94.07% of MySQL online submissions for Second Highest Salary.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
