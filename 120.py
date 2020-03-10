#120. Triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        s=[]
        for i in range(m):
            s.append([])
            for j in range(i+1):
                if i==m-1:
                    s[i].append(triangle[i][j])
                else:
                    s[i].append(0)
        for i in range(m-2,-1,-1):
            for j in range(i+1):
                s[i][j]=triangle[i][j]+min(s[i+1][j],s[i+1][j+1])
        return s[0][0]
#Runtime: 64 ms, faster than 35.95% of Python3 online submissions for Triangle.
#Memory Usage: 14.1 MB, less than 20.00% of Python3 online submissions for Triangle.