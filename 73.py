#73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col=[],[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)

        for i in row:
            for j in range(len(matrix[i])):
                matrix[i][j]=0 
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j]=0
#Runtime: 152 ms, faster than 75.38% of Python3 online submissions for Set Matrix Zeroes.
#Memory Usage: 14.5 MB, less than 5.10% of Python3 online submissions for Set Matrix Zeroes.