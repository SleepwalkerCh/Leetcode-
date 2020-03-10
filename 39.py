#39. Combination Sum
#背包问题,递归求解
class Solution:
    def combinationSum(self, candidates, target: int) :
        result=[]
        if not candidates:
            return result
        min=candidates[0]
        for i in candidates:
            if i<=min:
                min=i
        def Insert(candidates,target,now,edge):
            if target==0:
                result.append(now[:])
                return 0
            if target<min:
                return 0
            for i in range(edge,len(candidates)):
                if candidates[i]<=target:
                    now.append(candidates[i])
                    Insert(candidates,target-candidates[i],now,i)
                    now.pop()
        Insert(candidates,target,[],0)
        return result
sol=Solution()
print(sol.combinationSum([3,2,6,7],7))
#Runtime: 60 ms, faster than 91.92% of Python3 online submissions for Combination Sum.
#Memory Usage: 13.3 MB, less than 46.87% of Python3 online submissions for Combination Sum.
