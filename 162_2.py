#162. Find Peak Element
# 头升尾降，其中必有极值
# 二分法思路,时间复杂度满足要求
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums=nums
        return self.check(0,len(nums))

    def check(self,begin,end):
        if begin==end:
            return begin
        mid=(begin+end)//2
        if self.nums[mid]>self.nums[mid+1]:
            return self.check(begin,mid)
        else:
            return self.check(mid+1,end)
#Runtime: 40 ms, faster than 91.54% of Python3 online submissions for Find Peak Element.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.