#182. Duplicate Emails
# Write your MySQL query statement below
select Email from Person Group by Email having count(Email)>1
#Runtime: 263 ms, faster than 73.31% of MySQL online submissions for Duplicate Emails.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.