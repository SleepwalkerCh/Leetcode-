#79. Word Search
# 递归搜
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board=board
        self.word=word
        flag=[]
        for i in range(len(board)):
            flag.append([])
            for j in range(len(board[i])):
                flag[i].append(0)
        self.flag=flag
        if len(board)==0:
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    flag[i][j]=1
                    if len(word)==1:
                        return True
                    if self.search(i,j,1):
                        return True
                    flag[i][j]=0
        return False
    def search(self,x,y,num):
        print(x,y,num)
        if num>=len(self.word):
            return True

        if x!=0 and self.board[x-1][y]==self.word[num] and self.flag[x-1][y]==0:
            self.flag[x-1][y]=1
            if self.search(x-1,y,num+1):
                return True
            self.flag[x-1][y]=0
        if y!=0 and self.board[x][y-1]==self.word[num] and self.flag[x][y-1]==0:
            self.flag[x][y-1]=1
            if self.search(x,y-1,num+1):
                return True
            self.flag[x][y-1]=0
        if x!=len(self.board)-1 and self.board[x+1][y]==self.word[num] and self.flag[x+1][y]==0:
            self.flag[x+1][y]=1
            if self.search(x+1,y,num+1):
                return True
            self.flag[x+1][y]=0
        if y!=len(self.board[0])-1 and self.board[x][y+1]==self.word[num] and self.flag[x][y+1]==0:
            self.flag[x][y+1]=1
            if self.search(x,y+1,num+1):
                return True
            self.flag[x][y+1]=0
        return False
#Runtime: 428 ms, faster than 29.85% of Python3 online submissions for Word Search.
#Memory Usage: 15.3 MB, less than 16.17% of Python3 online submissions for Word Search.