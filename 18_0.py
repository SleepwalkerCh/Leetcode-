#18. 4Sum18
# 很简陋的做法，大概率会超时，在O(n^4)基础上做了一些小优化，但是结果未进行查重
# WRONG ANSWER
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        print(nums)
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    for l in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            result.append([nums[i],nums[j],nums[k],nums[l]])
                        if nums[i]+nums[j]+nums[k]+nums[l]>target:
                            break
        return result
            