#191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        s=0
        while n!=0:
            if n%2==1:
                s+=1
            n=n>>1
        return s
#Runtime: 32 ms, faster than 40.42% of Python3 online submissions for Number of 1 Bits.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.