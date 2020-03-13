#85. Maximal Rectangle
# 
class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix)==0:
            return 0
        maxnum=0
        columns=len(matrix[0])
        val=[0]*columns
        for row in matrix:
            for i in range(columns):
                val[i]=val[i]+1 if row[i]=="1" else 0
            for i in range(columns):
                minnum=val[i]
                for j in range(i,-1,-1):
                    if val[j]==0:
                        break
                    else:
                        if minnum>=val[j]:
                            minnum=val[j]
                        maxnum=max((i-j+1)*minnum,maxnum)
        return maxnum
#Runtime: 356 ms, faster than 25.21% of Python3 online submissions for Maximal Rectangle.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Maximal Rectangle.