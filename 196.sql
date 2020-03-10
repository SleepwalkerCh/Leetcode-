#196. Delete Duplicate Emails
# Write your MySQL query statement below
delete from Person where Id not in (select * from (select min(Id) from Person Group by Email) t)
#Runtime: 1211 ms, faster than 51.56% of MySQL online submissions for Delete Duplicate Emails.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.