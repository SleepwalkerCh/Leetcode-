#118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num=[]
        for i in range(numRows):
            num.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    num[i].append(1)
                else:
                    num[i].append(num[i-1][j-1]+num[i-1][j])
        return num
#Runtime: 32 ms, faster than 25.41% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.