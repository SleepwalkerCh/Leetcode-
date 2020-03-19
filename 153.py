# 153. Find Minimum in Rotated Sorted Array
# 加了一些临界判断的折半查找

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums[0],nums[1])
        if nums[len(nums)//2]<nums[0]:
            return self.findMin(nums[:len(nums)//2+1])
        else:
            return self.findMin(nums[len(nums)//2:])
#Runtime: 40 ms, faster than 59.47% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
#Memory Usage: 13.3 MB, less than 46.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.