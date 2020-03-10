# 52. N-Queens II
# 递归方法，应该会超时

class Solution:
    def totalNQueens(self, n: int) -> int:
        board=[]
        self.res=0
        for i in range(n):
            board.append([""])
            for j in range(n):
                board[i]+='.'
        self.board=board
        self.n=n
        self.Solving(0)
        return self.res
    def Solving(self,row):
        def check(board,x,y):
            flag=0
            for i in range(self.n):
                if board[i][y]=='Q':
                    if flag==1:
                        return False
                    else:
                        flag+=1
            #纵向
            flag=0
            for i in range(self.n):
                if x+y-i in range(self.n):
                    if board[i][x+y-i]=='Q':
                        if flag==1:
                            return False
                        else:
                            flag+=1
            flag=0
            for i in range(self.n):
                if i-x+y in range(self.n):
                    if board[i][i-x+y]=='Q':
                        if flag==1:
                            return False
                        else:
                            flag+=1
            return True
        if row==self.n:
            
            self.res+=1
            #print(result)
        else:
            i=row
            for j in range(self.n):
                self.board[i][j]="Q"
                if check(self.board,i,j):
                    self.Solving(i+1)
                self.board[i][j]="."
    


    
#Runtime: 304 ms, faster than 7.71% of Python3 online submissions for N-Queens.
#Memory Usage: 13.4 MB, less than 80.37% of Python3 online submissions for N-Queens.
                   