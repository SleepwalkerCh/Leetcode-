#85. Maximal Rectangle
# 搜索63/66，超时
class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix)==0:
            return 0
        self.column,self.row=len(matrix),len(matrix[0])
        self.matrix=matrix
        maxnum=0
        self.count=0
        for x in range(self.column):
            for y in range(self.row):
                if matrix[x][y]=="1"and maxnum<(self.column-x)*(self.row-y):
                    maxnum=max(maxnum,self.walk(x,y,x,y,x,y))
        print(self.count)
        return maxnum
    def walk(self,x,y,ax,ay,bx,by):
        val1,val2=0,0
        self.count+=1
        if ax==bx and ay==by:
            if ax+1<self.column:
                val1=self.walk(x,y,bx,by,bx+1,by)
            if ay+1<self.row:
                val2=self.walk(x,y,bx,by,bx,by+1)
            return max(val1,val2,1)
        else:
            if ax==bx:
                for i in range(x,ax+1):
                    if self.matrix[i][by]!="1":
                        return -1
                if bx+1<self.column and self.matrix[bx+1][by]=="1":
                    val1=self.walk(x,y,bx,by,bx+1,by)
                if by+1<self.row and self.matrix[bx][by+1]=="1":
                    val2=self.walk(x,y,bx,by,bx,by+1)
                return max(val1,val2,(by-y+1)*(bx-x+1))
            if ay==by:
                for i in range(y,by+1):
                    if self.matrix[bx][i]!="1":
                        return -1
                if bx+1<self.column  and self.matrix[bx+1][by]=="1":
                    val1=self.walk(x,y,bx,by,bx+1,by)
                if by+1<self.row  and self.matrix[bx][by+1]=="1":
                    val2=self.walk(x,y,bx,by,bx,by+1)
                return max(val1,val2,(by-y+1)*(bx-x+1))
matrix=[]
sol=Solution()
print(sol.maximalRectangle(matrix))