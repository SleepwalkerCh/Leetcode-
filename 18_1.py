#18. 4Sum
# 定好一个之后，思路和3SUM一样，速度还蛮快，可以用这个思路写N SUM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        if len(nums)<=3:
            return result
        for i in range(len(nums)-3):
            if nums[i]*4>target:
                break
            if nums[i]+3*nums[-1]<target:
                continue
            if i!=0 and nums[i]==nums[i-1]:
                continue
            newtarget=target-nums[i]
            for j in range(i+1,len(nums)-2):
                if nums[i]+nums[j]*3>target:
                    break
                if nums[i]+nums[j]+nums[-1]*2<target:
                    continue
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    if nums[j]+nums[k]+nums[l]==newtarget:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        #result.append([i,j,k,l])
                        l-=1
                        k+=1
                        while nums[k-1]==nums[k] and k<l:
                            k+=1
                        while nums[l+1]==nums[l] and k<l:
                            l-=1
                    elif nums[j]+nums[k]+nums[l]<newtarget:
                        k+=1
                        while nums[k-1]==nums[k] and k<l:
                            k+=1
                    else:
                        l-=1
                        while nums[l+1]==nums[l] and k<l:
                            l-=1
        return result
#Runtime: 112 ms, faster than 79.92% of Python3 online submissions for 4Sum.
#Memory Usage: 13.1 MB, less than 85.24% of Python3 online submissions for 4Sum.