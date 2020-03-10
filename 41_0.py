#41. First Missing Positive
# 试探一下时间复杂度,直接用set解决了问题，得到的数据结果很奇怪其实
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        for i in range(1,len(nums)+1):
            if not (i in nums):
                return i
        return i+1

#Runtime: 32 ms, faster than 93.26% of Python3 online submissions for First Missing Positive.
#Memory Usage: 13.3 MB, less than 29.67% of Python3 online submissions for First Missing Positive.
