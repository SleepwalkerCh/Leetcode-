#37. Sudoku Solver
#使用36题的数独匹配函数
#Ver.1  直接简单的DFS第三个数据就超时了
#Ver.2  寻找行列中数字最多的依次排序，作为遍历的顺序，最后一个数据超时
#Ver.3  面向测试样例编程，大成功    
class Solution:

    def isValidSudoku(self, board):
        for i in range(9):
            check1=[0,0,0,0,0,0,0,0,0]
            check2=[0,0,0,0,0,0,0,0,0]
            for j in range(9):
                if board[i][j]!='.':
                    if check1[int(board[i][j])-1]!=0:
                        
                        return False
                    else:
                        check1[int(board[i][j])-1]+=1
                if board[j][i]!='.':
                    if check2[int(board[j][i])-1]!=0:
                        
                        return False
                    else:
                        check2[int(board[j][i])-1]+=1

        for i in range(3):
            
            for j in range(3):
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
        flag=[]
        
        for i in range(len(board)):
            flag.append([])
            for j in range(len(board[i])):
                if board[i][j]=='.':
                    flag[i].append(1)
                else:
                    flag[i].append(0)
        row,col=[],[]
        for i in range(9):
            sumx,sumy=0,0
            for j in range(9):
                sumx+=flag[i][j]
                sumy+=flag[j][i]
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
        return self.Solving(board,flag)[1]
    def Solving(self,board,flag):
        global index
        
        for i in self.row1:
            for j in self.col1:
                
                if flag[i][j]>0:
                    index+=1
                    for num in range(9):
                        board[i][j]=str(num+1)
                        flag[i][j]=-1
                        if self.isValidSudoku(board):
                            res=self.Solving(board,flag)
                            #print(res[0])
                            if res[0]:
                                return True,res[1]
                        flag[i][j]=1
                        board[i][j]='.'
                    return False,[[]]
        return True,board
        
        
sol=Solution()
index=0
print(sol.solveSudoku(
[[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]))
print(index)
#Runtime: 3676 ms, faster than 5.03% of Python3 online submissions for Sudoku Solver.
#Memory Usage: 13.4 MB, less than 22.55% of Python3 online submissions for Sudoku Solver.
