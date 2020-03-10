#59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #54. Spiral Matrix
        if n==0:
            return [[]]
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        
        flag=[]
        for i in range(n):
            flag.append([])
            for j in range(n):
                flag[i].append(0)
        i,j,d=0,0,0
        danger=0
        num=2
        flag[0][0]=1
        while True:
            i+=direction[d%4][0]
            j+=direction[d%4][1]
            if  (not (i in range(n))) or (not (j in range(n))) or (flag[i][j]>0):
                if danger==0:
                    i-=direction[d%4][0]
                    j-=direction[d%4][1]
                    d+=1
                    danger=1
                else:
                    
                    break
            else:
                
                flag[i][j]=num
                num+=1
                danger=0
        return flag
#Runtime: 44 ms, faster than 15.19% of Python3 online submissions for Spiral Matrix II.
#Memory Usage: 13.7 MB, less than 5.17% of Python3 online submissions for Spiral Matrix II.