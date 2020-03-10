# 62. Unique Paths
#dynamic programming  
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num=[]
        for i in range(n):
            num.append([])
            for j in range(m):
                if i==0 or j==0:
                    num[i].append(1)
                else:
                    num[i].append(-1)
        for i in range(1,n):
            for j in range(1,m):
                if num[i][j]==-1:
                    num[i][j]=num[i-1][j]+num[i][j-1]
        return num[n-1][m-1]
#Runtime: 36 ms, faster than 67.66% of Python3 online submissions for Unique Paths.
#Memory Usage: 14 MB, less than 5.06% of Python3 online submissions for Unique Paths.