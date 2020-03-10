#81. Search in Rotated Sorted Array II
# 在33题基础上进行一些修改即可，32行内容，其实有32 的内容后面的判断也可以省略，显得简洁很多
# 二分情况可以用非递归方法来解决
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
                elif head>mid:
                    flag=3#轴在左侧
                else:
                    return max(searchNum(nums[len(nums)//2:],target,index+len(nums)//2),searchNum(nums[:len(nums)//2+1],target,index))
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
            return False
        if searchNum(nums,target,0)>=0:
            return True
        else:
            return False
#Runtime: 60 ms, faster than 86.10% of Python3 online submissions for Search in Rotated Sorted Array II.
#Memory Usage: 14.4 MB, less than 5.39% of Python3 online submissions for Search in Rotated Sorted Array II.