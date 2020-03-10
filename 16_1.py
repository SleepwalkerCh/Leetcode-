#16. 3Sum Closest
#很慢的三层循环，需要加速！

def threeSumClosest( nums, target: int) -> int:
    nums.sort()
    max=32767
    result=0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            num=target-nums[i]-nums[j]
            for t in range(j+1,len(nums)):
                if nums[t]>=num:
                    if t==j+1:
                        flag=j+1
                    else:
                        if abs(nums[t-1]-num)<abs(nums[t]-num):
                            flag=t-1
                        else:
                            flag=t
                    break
            if nums[-1]<num:
                flag=len(nums)-1
            if abs(nums[flag]-num)<=max:
                max=abs(nums[flag]-num)
                result=nums[flag]+nums[i]+nums[j]
    return result
print(threeSumClosest([1,-3,3,5,4,1],1))
#Runtime: 2232 ms, faster than 5.00% of Python3 online submissions for 3Sum Closest.
#Memory Usage: 13 MB, less than 89.25% of Python3 online submissions for 3Sum Closest.
