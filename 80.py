#80. Remove Duplicates from Sorted Array II
#俩指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        i,j=0,1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
                while j<len(nums):
                    if nums[i]==nums[j]:
                        nums.pop(j)
                    else:
                        i=j
                        j+=1
            else:
                i+=1
                j+=1
        return len(nums)
#Runtime: 80 ms, faster than 10.80% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Memory Usage: 13.8 MB, less than 5.30% of Python3 online submissions for Remove Duplicates from Sorted Array II.
