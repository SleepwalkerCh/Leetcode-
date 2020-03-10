# 198. House Robber
# 类似动态规划思路
class Solution:
    def rob(self, nums: List[int]) -> int:
        num=[]
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        for i in range(len(nums)):
            if i>=3:
                num.append(max(nums[i]+num[i-2],nums[i]+num[i-3],num[i-1]))
            elif i>=2:
                num.append(max(nums[i]+num[i-2],num[i-1]))
            elif i==1:
                num.append(max(num[i-1],nums[i]))
            else:
                num.append(nums[i])
        return num[len(nums)-1]
#Runtime: 28 ms, faster than 73.75% of Python3 online submissions for House Robber.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for House Robber.