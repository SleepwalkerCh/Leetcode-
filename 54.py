#54. Spiral Matrix
#直接遍历
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        res=[]
        flag=[]
        for i in range(len(matrix)):
            flag.append([])
            for j in range(len(matrix[i])):
                flag[i].append(0)
        i,j,d=0,0,0
        danger=0
        res.append(matrix[0][0])
        flag[0][0]=1
        while True:
            
            i+=direction[d%4][0]
            j+=direction[d%4][1]
            if  (not (i in range(len(matrix)))) or (not (j in range(len(matrix[0])))) or (flag[i][j]==1):
                if danger==0:
                    i-=direction[d%4][0]
                    j-=direction[d%4][1]
                    d+=1
                    danger=1
                else:
                    
                    break
            else:
                res.append(matrix[i][j])
                flag[i][j]=1
                danger=0
        return res
#Runtime: 32 ms, faster than 86.30% of Python3 online submissions for Spiral Matrix.
#Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Spiral Matrix.