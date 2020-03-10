#47. Permutations II
#套用46题的递归，更改了flag通过的逻辑关系即可通过
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        flag=[]
        for i in range(len(nums)):
            flag.append(True)
        def P(nums,no,now):
            if no==len(nums):
                res.append(now[:])
            else:
                for i in range(len(nums)):
                    if flag[i] and (i==0 or (i!=0 and nums[i]!=nums[i-1] or (nums[i]==nums[i-1] and not flag[i-1]))):
                        now.append(nums[i])
                        flag[i]=False
                        P(nums,no+1,now)
                        flag[i]=True
                        now.pop()
        P(nums,0,[])
        return res
#Runtime: 76 ms, faster than 57.03% of Python3 online submissions for Permutations II.
#Memory Usage: 13.4 MB, less than 47.64% of Python3 online submissions for Permutations II.
