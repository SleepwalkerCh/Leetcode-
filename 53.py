# 53. Maximum Subarray
# 很快的动态规划方法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=-2147483648
        maxnum=[]
        if not nums:
            return res
        
        maxnum.append(nums[0])
        res=maxnum[-1]
        
        for i in range(1,len(nums)):
            if maxnum[i-1]>=0:
                maxnum.append(nums[i]+maxnum[i-1])
            else:
                maxnum.append(nums[i])
            if maxnum[-1]>res:
                res=maxnum[-1]
        return res
#Runtime: 36 ms, faster than 96.78% of Python3 online submissions for Maximum Subarray.
#Memory Usage: 14.1 MB, less than 9.22% of Python3 online submissions for Maximum Subarray.

#[-2,1,-3,4,-1,2,1,-5,4]
#[-2,1,-2,4,3,5,6,-1,3]