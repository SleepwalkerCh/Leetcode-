#37. Sudoku Solver
#使用36题的数独匹配函数
#Ver.1  直接简单的DFS第三个数据就超时了
#Ver.2  寻找行列中数字最多的依次排序，作为遍历的顺序，最后一个数据超时
#Ver.3  面向测试样例编程，大成功    
#Ver.4  简化数独匹配函数，速度加快了很多 
class Solution:

    def isValidSudoku(self, board,x,y):
        check1=[0,0,0,0,0,0,0,0,0]
        check2=[0,0,0,0,0,0,0,0,0]
        for j in range(9):
            if board[x][j]!='.':
                if check1[int(board[x][j])-1]!=0:
                    
                    return False
                else:
                    check1[int(board[x][j])-1]+=1
            if board[j][y]!='.':
                if check2[int(board[j][y])-1]!=0:
                    
                    return False
                else:
                    check2[int(board[j][y])-1]+=1

        i=x//3
        j=y//3
        check=[0,0,0,0,0,0,0,0,0]
        for i1 in range(3):
            for j1 in range(3):
                if board[i*3+i1][j*3+j1]!='.':
                    if check[int(board[i*3+i1][j*3+j1])-1]!=0:
                        return False
                    else:
                        check[int(board[i*3+i1][j*3+j1])-1]+=1
        return True
    
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        

        row,col=[],[]
        for i in range(9):
            sumx,sumy=0,0
            for j in range(9):
                if board[i][j]=='.':
                    sumx+=1
                if board[j][i]=='.':
                    sumy+=1
            row.append((sumx,i))
            col.append((sumy,i))
        def takeFirst(elem):
            return elem[0]
        row.sort(key=takeFirst)
        col.sort(key=takeFirst)
        
        row1,col1=[],[]
        for i in row:
            row1.append(i[1])
        for i in col:
            col1.append(i[1])
        
        self.row1=row1
        self.col1=col1
        board= self.Solving(board)[1]
    def Solving(self,board):
       
        
        for i in self.row1:
            for j in self.col1:
                
                if board[i][j]=='.':
                    
                    for num in range(9):
                        board[i][j]=str(num+1)
                        
                        if self.isValidSudoku(board,i,j):
                            res=self.Solving(board)
                            #print(res[0])
                            if res[0]:
                                return True,res[1]
                        
                        board[i][j]='.'
                    return False,[[]]
        return True,board
        
        

        
        
sol=Solution()
index=0
print(sol.solveSudoku(
[[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]))
print(index)
