#180. Consecutive Numbers
select DISTINCT  Num as ConsecutiveNums from Logs where (Id+1,Num) In (select * from Logs where (Id+1,Num) In (select * from Logs))
#Runtime: 842 ms, faster than 31.47% of MySQL online submissions for Consecutive Numbers.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Consecutive Numbers.