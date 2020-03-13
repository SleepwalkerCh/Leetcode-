#162. Find Peak Element
# 遍历，非递增项
# 测时间效率
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1
#Runtime: 40 ms, faster than 91.54% of Python3 online submissions for Find Peak Element.
#Memory Usage: 13 MB, less than 94.12% of Python3 online submissions for Find Peak Element.