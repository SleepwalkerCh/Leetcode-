#45. Jump Game II
#简单的贪心递归，将之前那一版的递归改成了递推就过了
#好像是BFS来着，其实改进的地方可以直接把前面数据初始化给删了
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        record=[]
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            if nums[i]+i>len(nums)-1:
                target=len(nums)-1
            else:
                target=nums[i]+i
            record.append(target)
        '''
        i=0  
        step=1
        while i<len(nums):
            tmax,imax=-1,-1
            if record[i]==len(nums)-1:
                break
            if nums[i]+i>len(nums)-1:
                target=len(nums)-1
            else:
                target=nums[i]+i
            for j in range(i+1,target+1):
                if nums[j]+j>len(nums)-1:
                    target1=len(nums)-1
                else:
                    target1=nums[i]+i
                if tmax<target1:
                    tmax=target1
                    imax=j
            i=imax
            step+=1
        return step
#Runtime: 72 ms, faster than 13.54% of Python3 online submissions for Jump Game II.
#Memory Usage: 15.5 MB, less than 7.02% of Python3 online submissions for Jump Game II.
#Ver 2.0
#Runtime: 60 ms, faster than 34.72% of Python3 online submissions for Jump Game II.
#Memory Usage: 14.7 MB, less than 20.92% of Python3 online submissions for Jump Game II.