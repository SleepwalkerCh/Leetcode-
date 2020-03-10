#46. Permutations
# 递归做一个全排列的题
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        flag=[]
        for i in range(len(nums)):
            flag.append(True)
        def P(nums,no,now):
            if no==len(nums):
                res.append(now[:])
            else:
                for i in range(len(nums)):
                    if flag[i]:
                        now.append(nums[i])
                        flag[i]=False
                        P(nums,no+1,now)
                        flag[i]=True
                        now.pop()
        P(nums,0,[])
        return res
#Runtime: 52 ms, faster than 67.95% of Python3 online submissions for Permutations.
#Memory Usage: 13.4 MB, less than 23.77% of Python3 online submissions for Permutations.