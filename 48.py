#48. Rotate Image
#简单的几何题
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i,j=0,0
        n=len(matrix)
        def swap(matrix,x,y,n):
            temp=matrix[x,y]
            matrix[x,y]=matrix[n-y][x]
            matrix[n-y][x]=matrix[n-x][n-y]
            matrix[n-x][n-y]=matrix[y][n-x]
            matrix[y][n-x]=temp
        for i in range((n+1)//2):
            for j in range(n//2):
                swap(matrix,i,j,n)
#Runtime: 36 ms, faster than 83.43% of Python3 online submissions for Rotate Image.
#Memory Usage: 13.1 MB, less than 67.37% of Python3 online submissions for Rotate Image.
    