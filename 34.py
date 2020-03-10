# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def isIn(nums:List[int],target:int):
            head,tail=0,len(nums)-1
            if len(nums)==1 and nums[head]==target:
                return True
            while head<tail:
                mid=(head+tail)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    head=mid+1
                else:
                    tail=mid
            return False
        if not isIn(nums,target):
            return [-1,-1]
        else:
            head,tail=0,len(nums)-1
            while head<tail:
                mid=(head+tail)//2
                if target<=nums[mid]:
                    tail=mid
                else:
                    head=mid+1
            a=head
            head,tail=0,len(nums)-1
            if target==nums[tail]:
                head=len(nums)
            else:
                while head<tail:
                    mid=(head+tail)//2
                    if target<nums[mid]:
                        tail=mid
                    else:
                        head=mid+1
            b=head-1
            return [a,b]      
# Runtime: 40 ms, faster than 66.86% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 13.9 MB, less than 32.70% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.