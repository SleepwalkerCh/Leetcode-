#41. First Missing Positive
# 老凯做法，真正的O(n)复杂度实现方法
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        length=len(nums)
        while i<length:
            if i==nums[i]-1:
                i+=1
                continue
            if nums[i]>0 and nums[i]<=length and nums[nums[i]-1]!=nums[i] :
                temp=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=temp
            else:
                nums[i]=0
                i+=1
        for i in range(length):
            if nums[i]==0:
                return i+1
        return length+1
#Runtime: 36 ms, faster than 77.98% of Python3 online submissions for First Missing Positive.
#Memory Usage: 13.3 MB, less than 8.55% of Python3 online submissions for First Missing Positive.