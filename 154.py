# 154. Find Minimum in Rotated Sorted Array II
# 增加了相等情况的判断
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums[0],nums[1])
        left,right=nums[0],nums[-1]
        if nums[len(nums)//2]<=nums[0]:
            left=self.findMin(nums[:len(nums)//2+1])
        if nums[len(nums)//2]>=nums[-1]:
            right=self.findMin(nums[len(nums)//2:])
        return min(left,right)
#Runtime: 56 ms, faster than 37.90% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
#Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.