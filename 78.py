#78. Subsets
# 套用77题的全排列
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.result=result
        for i in range(len(nums)+1):
            self.Combination(nums,i,[]])
        return self.result

    def Combination(self,nums,num,res): 
        if num==0:
            self.result.append(res[:])
        for i in range(len(nums)):
            res.append(nums[i])
            self.Combination(nums[i+1:],num-1,res)
            del(res[-1])
#Runtime: 48 ms, faster than 17.59% of Python3 online submissions for Subsets.
#Memory Usage: 14.1 MB, less than 5.06% of Python3 online submissions for Subsets.