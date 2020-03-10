# 130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        self.flag=[]
        
        for i in range(len(board)):
            self.flag.append([])
            for j in range(len(board[i])):
                num=-1 if board[i][j]=='X' else 0
                self.flag[i].append(num)
        
        for i in range(len(board)):
            if self.flag[i][0]==0:
                self.check(i,0)
            if self.flag[i][len(board[0])-1]==0:
                self.check(i,len(board[0])-1)
        for i in range(len(board[0])):
            if self.flag[0][i]==0:
                self.check(0,i)
            if self.flag[len(board)-1][i]==0:  
                self.check(len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.flag[i][j]==1:
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        print(self.flag)
        return
    def check(self,i,j):
        self.flag[i][j]=1
        if i+1<len(self.flag):
            if self.flag[i+1][j]==0:
                self.check(i+1,j)
        if i-1>=0:
            if self.flag[i-1][j]==0:
                
                self.check(i-1,j)
        if j+1<len(self.flag[0]):
            if self.flag[i][j+1]==0:
                self.check(i,j+1)
        if j-1>=0:
            if self.flag[i][j-1]==0:
                self.check(i,j-1)
        return 
#Runtime: 148 ms, faster than 58.53% of Python3 online submissions for Surrounded Regions.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Surrounded Regions.