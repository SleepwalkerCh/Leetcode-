#75. Sort Colors
#这应该是只遍历一次的结果
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero,two=0,len(nums)-1
        i=0
        while i<len(nums):
            if nums[i]==0:
                temp=nums[i]
                nums[i]=nums[zero]
                nums[zero]=temp
                while nums[zero]==0:
                    zero+=1
            elif nums[i]==2:
                temp=nums[i]
                nums[i]=nums[two]
                nums[two]=temp
                while nums[two]==0:
                    two+=1
                
            i+=1
#Runtime: 32 ms, faster than 98.86% of Python3 online submissions for Sort Colors.
#Memory Usage: 13.9 MB, less than 5.35% of Python3 online submissions for Sort Colors.