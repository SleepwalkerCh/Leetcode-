# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        
        res=0
        self.grid=grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]=="1":
                    self.check(i,j)
                    res+=1
        
        return res
    def check(self,i,j):
        self.grid[i][j]="0"
        if i+1<len(self.grid):
            if self.grid[i+1][j]=="1":
                self.check(i+1,j)
        if i-1>=0:
            if self.grid[i-1][j]=="1":
                
                self.check(i-1,j)
        if j+1<len(self.grid[0]):
            if self.grid[i][j+1]=="1":
                self.check(i,j+1)
        if j-1>=0:
            if self.grid[i][j-1]=="1":
                self.check(i,j-1)
        return 
#Runtime: 136 ms, faster than 88.44% of Python3 online submissions for Number of Islands.
#Memory Usage: 13.7 MB, less than 88.89% of Python3 online submissions for Number of Islands.