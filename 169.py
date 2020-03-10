# 169. Majority Element
# Boyer-Moore Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        flag,num=0,0
        for i in nums:
            if flag == 0:
                num=i
                flag+=1
            else:
                flag+=1 if num==i else -1
        return num
#Runtime: 184 ms, faster than 46.94% of Python3 online submissions for Majority Element.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Majority Element.