# 52. N-Queens II
# 递归方法，应该会超时
# 尝试将其变为非递归方式

class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(board,x,y):
            flag=0
            for i in range(n):
                if board[i][y]=='Q':
                    if flag==1:
                        return False
                    else:
                        flag+=1
            #纵向
            flag=0
            for i in range(n):
                if x+y-i in range(n):
                    if board[i][x+y-i]=='Q':
                        if flag==1:
                            return False
                        else:
                            flag+=1
            flag=0
            for i in range(n):
                if i-x+y in range(n):
                    if board[i][i-x+y]=='Q':
                        if flag==1:
                            return False
                        else:
                            flag+=1
            return True
        def search(board,x):
            for i in range(len(board[x])):
                if board[x][i]=='Q':
                    return i
        board=[]
        res=0
        if n==1:
            return 1
        for i in range(n):
            board.append([""])
            for j in range(n):
                board[i]+='.'
        i,j=0,0
        #global index
        while True:
            #结束判定
            #index+=1
            if i==0 and j==n:
                break
            # 满足条件的一组N皇后
            if i==n:
                res+=1
                i-=1
                board[i][search(board,i)]='.'
                i-=1
                j=search(board,i)
                board[i][j]='.'
                j+=1
            elif j==n:
                i-=1
                j=search(board,i)
                board[i][j]='.'
                j+=1
            else:
                board[i][j]='Q'
                if not check(board,i,j):
                    board[i][j]='.'
                    j+=1
                    continue
                else:
                    i+=1
                    j=0
                    continue
        return res
sol=Solution()
index=0
print(sol.totalNQueens(11))
print(index)
#Runtime: 256 ms, faster than 5.53% of Python3 online submissions for N-Queens II.
#Memory Usage: 13.6 MB, less than 5.63% of Python3 online submissions for N-Queens II.