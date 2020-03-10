#74. Search a 2D Matrix
# 完成过程中很多粗心小错误，以后应该多加练习二分法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        i,j=0,len(matrix)-1
        while i<j:
            num=(i+j+1)//2
            if matrix[num][0]>target:
                j=num-1
            elif matrix[num][0]<target:
                i=num
            else:
                return True
        if matrix[i][0]==target:
            return True
        if i==0:
            if matrix[0][0]>target:
                return False
        t=i
        i,j=0,len(matrix[t])-1
        while i<j:
            num=(i+j)//2
            if matrix[t][num]>target:
                j=num
            elif matrix[t][num]<target:
                i=num+1
            else:
                return True
        if matrix[t][i]==target:
            return True
        return False
#Runtime: 72 ms, faster than 94.27% of Python3 online submissions for Search a 2D Matrix.
#Memory Usage: 15.8 MB, less than 5.02% of Python3 online submissions for Search a 2D Matrix.