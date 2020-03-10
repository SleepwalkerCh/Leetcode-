#189. Rotate Array
#一步步移动，直接做会超时 v1.1
#分左移右移做,还是会超时 v1.2

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=0
        if (-k)%len(nums)<(k%len(nums)):
            for i in range((-k)%len(nums)):
                temp=nums[0]
                for j in range(len(nums)-1):
                    nums[j]=nums[j+1]
                nums[len(nums)-1]=temp
        else:
            for i in range(k%len(nums)):
                temp=nums[len(nums)-1]
                for j in range(len(nums)-1):
                    nums[len(nums)-j-1]=nums[len(nums)-j-2]
                nums[0]=temp
        return nums