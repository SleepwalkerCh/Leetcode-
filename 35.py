# 35. Search Insert Position
# 简单的二分查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        head,tail=0,len(nums)-1
        #========这段特殊情况的处理可以省略================
        if len(nums)==0:
            return 0
        if target<nums[head]:
            return 0
        if target>nums[tail]:
            return len(nums)
        #============================================
        while head<tail:
            mid=(head+tail)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                tail=mid
            else:
                head=mid+1
        return head
#Runtime: 36 ms, faster than 75.53% of Python3 online submissions for Search Insert Position.
#Memory Usage: 13.8 MB, less than 30.42% of Python3 online submissions for Search Insert Position.

0 1 3 4