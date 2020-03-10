#36. Valid Sudoku
# 简单的遍历即可
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check1=[0,0,0,0,0,0,0,0,0]
            check2=[0,0,0,0,0,0,0,0,0]
            for j in range(9):
                if board[i][j]!='.':
                    if check1[int(board[i][j])-1]!=0:
                        print(i,j)
                        return False
                    else:
                        check1[int(board[i][j])-1]+=1
                if board[j][i]!='.':
                    if check2[int(board[j][i])-1]!=0:
                        print(i,j)
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
#Runtime: 40 ms, faster than 98.47% of Python3 online submissions for Valid Sudoku.
#Memory Usage: 13.2 MB, less than 56.26% of Python3 online submissions for Valid Sudoku.