#70. Climbing Stairs
#a[i]=a[i-1]+a[i-2] 好像有点慢

class Solution:
    def climbStairs(self, n: int) -> int:
        
        i,j=1,2
        numi,numj=1,2
        while j<=n:
            
            temp=numi
            numi=numj
            numj=temp+numj
            i+=1
            j+=1
        return numj
#Runtime: 64 ms, faster than 5.76% of Python3 online submissions for Climbing Stairs.
#Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Climbing Stairs.            