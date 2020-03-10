#84. Largest Rectangle in Histogram
# 建立二维表方式超时
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=[]
        if len(heights)==0:
            return 0
        nmax=-1
        for i in range(len(heights)):
            res.append([])
            for j in range(len(heights)):
                if i==j:
                    res[i].append([heights[i],1])
                    if nmax<heights[i]:
                        nmax=heights[i]
                    
                res[i].append([-1,j-i+1])
        
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[j]>res[i][j-1][0]:
                    res[i][j]=[res[i][j-1][0],j-i+1]
                else:
                    res[i][j]=[heights[j],j-i+1]
                if res[i][j][0]*res[i][j][1]>nmax:
                    nmax=res[i][j][0]*res[i][j][1]
        return nmax