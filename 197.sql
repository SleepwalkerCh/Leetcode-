#197. Rising Temperature
# Write your MySQL query statement below
select b.Id from Weather a,Weather b where DATE_ADD(a.RecordDate,INTERVAL 1 DAY)=b.RecordDate and a.Temperature<b.Temperature
#Runtime: 439 ms, faster than 75.73% of MySQL online submissions for Rising Temperature.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.