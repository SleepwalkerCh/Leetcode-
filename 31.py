#31. Next Permutation
# 从后往前找到首个非递增数列的那一位，再将后面的数列逆序
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        
        for i in range(len(nums)-1):
        
            if nums[-1-i]>nums[-2-i]:
                pos=len(nums)-2-i
                break
        pos2=len(nums)-1
        for i in range(pos+1,len(nums)):
            if nums[pos]>=nums[i]:
                pos2=i-1
                break
        def swap(i,j):
            t=nums[i]
            nums[i]=nums[j]
            nums[j]=t
        swap(pos,pos2)
        i=1
        while len(nums)-i>pos+i:
            swap(len(nums)-i,pos+i) 
            i+=1
#Runtime: 36 ms, faster than 96.82% of Python3 online submissions for Next Permutation.
#Memory Usage: 13.3 MB, less than 28.75% of Python3 online submissions for Next Permutation.



# 1,3,2,4
# 1,2,5,4,3 -> 1,3,2,4,5   
# -1 5 0 4 1 3 
# 1,2,4,5,4,3->1,2,5,3,4,4
# 1,5,8,7,6,4,3,2->[1,6,2,3,4,5,7,8]