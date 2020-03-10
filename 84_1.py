#84. Largest Rectangle in Histogram
# 参照讨论里面的思路，动态规划实现
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        Left,Right=[],[]
        for i in heights:
            Left.append(-1)
            Right.append(-1)
        Left[0]=0
        Right[-1]=len(heights)-1
        for i in range(1,len(heights)):
            j=i-1
            while True:
                if j<0:
                    Left[i]=0
                    break
                if heights[j]<heights[i]:
                    Left[i]=j+1
                    break
                else:
                    j=Left[j]-1
        for i in range(len(heights)-2,-1,-1):
            j=i+1
            while True:
                if j>len(heights)-1:
                    Right[i]=len(heights)-1
                    break
                if heights[j]<heights[i]:
                    Right[i]=j+1
                    break
                else:
                    j=Right[j]+1
        nmax=-1
        for i in range(len(heights)):
            nmax=max(nmax,heights[i]*(Right[i]-Left[i]+1))
        return nmax
#Runtime: 140 ms, faster than 15.36% of Python3 online submissions for Largest Rectangle in Histogram.
#Memory Usage: 16.6 MB, less than 8.34% of Python3 online submissions for Largest Rectangle in Histogram
                