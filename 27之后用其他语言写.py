#27. Remove Element
#这道题用python语言写出来感觉没什么意义
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
#Runtime: 36 ms, faster than 80.64% of Python3 online submissions for Remove Element.
#Memory Usage: 13.2 MB, less than 50.83% of Python3 online submissions for Remove Element.      