#162. Find Peak Element
#一般条件下时间复杂度不理想
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        return self.check(nums)
    def check(self,nums):
        print(nums)
        if len(nums)==2:
            return -1
        mid=len(nums)//2
        if nums[mid]>max(nums[mid+1],nums[mid-1]):
            return mid
        if nums[0]>nums[mid]:
            val=self.check(nums[:mid+1])
            if val!=-1:
                return val
            else:
                return -1
        if nums[len(nums)-1]>nums[mid]:
            val=self.check(nums[mid:])
            if val!=-1:
                return mid+val
            else:
                return -1
        v1=self.check(nums[:mid+1])
        v2=self.check(nums[mid:])
        if max(v1,v2)==-1:
            return -1
        else:
            if v1!=-1:
                return v1
            else:
                return mid+v2
        
#Runtime: 44 ms, faster than 73.27% of Python3 online submissions for Find Peak Element.
#Memory Usage: 13 MB, less than 94.12% of Python3 online submissions for Find Peak Element.