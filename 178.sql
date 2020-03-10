178. Rank Scores
# Write your MySQL query statement below
SELECT score,(select count(distinct score) from scores where a.score<=score) as Rank FROM Scores a order by score DESC

#Runtime: 1062 ms, faster than 17.95% of MySQL online submissions for Rank Scores.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.