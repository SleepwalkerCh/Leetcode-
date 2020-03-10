#45. Jump Game II
# 抄袭55的思路，简单的遍历，感觉有些慢
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res=[]
        for i in nums:
            res.append(-1)
        res[0]=0
        i=0
        while i<len(res)-1:
            if res[i]>=0:
                if i+nums[i]>len(res)-1:
                    target=len(res)-1
                else:
                    target=i+nums[i]
                
                for j in range(i+1,target+1):
                    if j>=len(res):
                        break
                    if res[j]==-1:
                        res[j]=res[i]+1
                    elif res[i]+1<res[j]:
                        res[j]=res[i]+1
            
            i+=1
        return res[-1]
#果然超时没过
