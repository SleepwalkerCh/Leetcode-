#190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        num=0
        for i in range(31):
            num+=n%2
            num=num<<1
            n=n>>1
        return num
#Runtime: 28 ms, faster than 76.79% of Python3 online submissions for Reverse Bits.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Bits.