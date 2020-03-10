#77. Combinations
#简单的全排列
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.result=result
        nums=[x+1 for x in range(n-1)]
        self.Combination(nums,k,[])
        return self.result
    def Combination(self,nums,num,res): 
        if num==0:
            self.result.append(res[:])
        for i in range(len(nums)):
            res.append(nums[i])
            self.Combination(nums[i+1:],num-1,res)
            del(res[-1])
#Runtime: 696 ms, faster than 20.81% of Python3 online submissions for Combinations.
#Memory Usage: 15.3 MB, less than 19.18% of Python3 online submissions for Combinations.