# 33. Search in Rotated Sorted Array
# 考虑长度为0,1,2的特殊情况，对轴的位置进行分类并进行处理，使用二分法使得时间复杂度满足条件
class Solution:
    def search(self, nums, target: int) -> int:
        def searchNum(nums, target: int, index:int) -> int:
            #=========特殊情况与相等判定=========#
            head=nums[0]
            tail=nums[-1]
            mid=nums[len(nums)//2]
            if len(nums)==1 and head!=target:
                return -1
            if len(nums)==2 and head!=target and tail!=target:
                return -1
            if head==target:
                return index
            if tail==target:
                return index+len(nums)-1
            if mid==target:
                return index+len(nums)//2
            if head>target and tail<target:
                return -1
            #============分情况=================#  
            flag=0
            if head<tail:
                flag=1#升序，无轴
            else:
                if head<mid:
                    flag=2# 轴在右侧
                else:
                    flag=3#轴在左侧
            if flag==1:
                if target<head or target>tail:
                    return -1
                elif target>mid:
                    return searchNum(nums[len(nums)//2:],target,index+len(nums)//2)
                else:
                    return searchNum(nums[:len(nums)//2+1],target,index)
            elif flag==2:
                if target>head and target<mid:
                    return searchNum(nums[:len(nums)//2+1],target,index)
                if target<tail or target>mid:
                    return searchNum(nums[len(nums)//2:],target,index+len(nums)//2)
            else:
                if target>mid and target<tail:
                    return searchNum(nums[len(nums)//2:],target,index+len(nums)//2)
                if target>head or target<mid:
                    return searchNum(nums[:len(nums)//2+1],target,index)
        
        if len(nums)==0:
            return -1
        else:
            return searchNum(nums,target,0)
sol=Solution()
a=[7,8,9,10,1,2,3,4,5,6]
print(sol.search(a,10))
# Runtime: 36 ms, faster than 76.57% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.1 MB, less than 92.07% of Python3 online submissions for Search in Rotated Sorted Array.

#0 1 2 3  4 5 6 7 8 9 #3
#7 8 9 10 1 2 3 4 5 6
#7 1 6
#0 1 2 3 4 5 6  7 8 9  #2
#4 5 6 7 8 9 10 1 2 3
#4 8 3
