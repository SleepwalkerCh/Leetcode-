#189. Rotate Array
# 根据hint思路，进行reverse操作
# 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums=self.reverse(nums,0,len(nums)-1)
        k=k % len(nums)
        nums=self.reverse(nums,0,k-1)
        nums=self.reverse(nums,k,len(nums)-1)
        return nums
    def reverse(self,nums,begin,end):
        while begin<end:
            temp=nums[begin]
            nums[begin]=nums[end]
            nums[end]=temp
            begin+=1
            end-=1
        return nums
#Runtime: 64 ms, faster than 57.96% of Python3 online submissions for Rotate Array.
#Memory Usage: 14.1 MB, less than 5.09% of Python3 online submissions for Rotate Array.
