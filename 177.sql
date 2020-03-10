# 177. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE T INT;
  SET T=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee order by Salary desc limit T,1
  );
END
#Runtime: 801 ms, faster than 9.66% of MySQL online submissions for Nth Highest Salary.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Nth Highest Salary.