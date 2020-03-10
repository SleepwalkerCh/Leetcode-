#64. Minimum Path Sum
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num=[]
        for i in range(len(grid)):
            num.append([])
            for j in range(len(grid[i])):
                if i==0 or j==0:
                    if i==0 and j!=0:
                        num[i].append(num[i][j-1]+grid[i][j])
                    elif i!=0 and j==0:
                        num[i].append(num[i-1][j]+grid[i][j])
                    else:
                        num[i].append(grid[i][j])
                else:
                    num[i].append(-1)
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                if num[i][j]==-1:
                    num[i][j]=min(num[i-1][j],num[i][j-1])+grid[i][j]
        
        return num[len(grid)-1][len(grid[0])-1]
#Runtime: 120 ms, faster than 5.09% of Python3 online submissions for Minimum Path Sum.
#Memory Usage: 16 MB, less than 8.86% of Python3 online submissions for Minimum Path Sum.