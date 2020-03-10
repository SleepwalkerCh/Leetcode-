#42. Trapping Rain Water
# 一个可以看作是数学题的方法解题，
class Solution:
    def trap(self, height: List[int]) -> int:
        nummax,imax=0,0
        water=height[:]
        for i in range(len(height)):
            if height[i]>=nummax:
                nummax=height[i]
                imax=i
        i=0
        while i<imax:
            j=i+1
            while j<imax and height[j]<height[i]:
                j+=1
            for k in range(i,j+1):
                water[k]=height[i]
            i=j
        i=len(height)-1
        while i>imax:
            j=i-1
            while j>imax and height[j]<height[i]:
                j-=1
            for k in range(j,i+1):
                water[k]=height[i]
            i=j
        print(water)
        sum=0
        for i in range(len(height)):
            if water[i]>height[i]:
                sum+=water[i]-height[i]
        return sum
#Runtime: 44 ms, faster than 64.35% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 13.6 MB, less than 62.95% of Python3 online submissions for Trapping Rain Water.