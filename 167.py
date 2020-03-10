#167. Two Sum II - Input array is sorted
#双指针找到结果 贪心算法
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while numbers[i]+numbers[j]!=target:
            if numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
        return [i+1,j+1]
#Runtime: 64 ms, faster than 67.86% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.