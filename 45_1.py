#45. Jump Game II
#还是超时，简单的递归
class Solution:
    def jump(self, nums: List[int]) -> int:

        def Gojump(index,step):
            if index==0:
                return step
            else:
                for i in range(index):
                    if i+nums[i]>=index:
                        return Gojump(i,step+1)
        return Gojump(len(nums),0)