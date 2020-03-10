#26. Remove Duplicates from Sorted Array
#和27题做法一样，这题看起来没什么意义
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        if not nums:
            return 0
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
            
            
            
#Runtime: 76 ms, faster than 30.98% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 14.8 MB, less than 56.89% of Python3 online submissions for Remove Duplicates from Sorted Array.