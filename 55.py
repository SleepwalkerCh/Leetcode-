#55. Jump Game
# 简单的遍历，感觉有些慢
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=[]
        for i in nums:
            res.append(False)
        res[0]=True
        i=0
        while i<len(res)-1:
            if res[i]:
                if i+nums[i]>len(res)-1:
                    target=len(res)-1
                else:
                    target=i+nums[i]
                if not res[target]:  
                    for j in range(i+1,target+1):
                        if j>=len(res):
                            break
                        res[j]=True
            if res[-1]:
                return True
            i+=1
        return res[-1]
#Runtime: 64 ms, faster than 13.14% of Python3 online submissions for Jump Game.
#Memory Usage: 14.3 MB, less than 98.21% of Python3 online submissions for Jump Game.