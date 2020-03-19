#152. Maximum Product Subarray
# 同时记录下max和min的dp
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        pos,neg,res=0,0,0
        for i in nums:
            pos,neg=max(neg*i,pos*i,i),min(neg*i,pos*i,i)
            if res<pos:
                res=pos
        return res
#Runtime: 52 ms, faster than 83.17% of Python3 online submissions for Maximum Product Subarray.
#Memory Usage: 13.1 MB, less than 96.55% of Python3 online submissions for Maximum Product Subarray.