# 40 Combination Sum II
#用39题的思路直接移植，并对重复数情况进行筛除
class Solution:
    def combinationSum2(self, candidates, target: int) :
        candidates.sort()
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
            for i in range(edge+1,len(candidates)):
                if i!=0 and i!=edge+1 and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]<=target:
                    now.append(candidates[i])
                    Insert(candidates,target-candidates[i],now,i)
                    now.pop()
        Insert(candidates,target,[],-1)
        return result
sol=Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5],8))
#Runtime: 60 ms, faster than 69.91% of Python3 online submissions for Combination Sum II.
#Memory Usage: 13.2 MB, less than 60.91% of Python3 online submissions for Combination Sum II.