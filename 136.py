#136. Single Number
# 用位运算
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=0
        for i in nums:
            num^=i
        return num
#Runtime: 88 ms, faster than 67.27% of Python3 online submissions for Single Number.
#Memory Usage: 15.3 MB, less than 8.20% of Python3 online submissions for Single Number.