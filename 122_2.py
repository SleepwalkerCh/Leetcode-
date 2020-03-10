#  122. Best Time to Buy and Sell Stock II
#  简单方法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                s+=prices[i+1]-prices[i]
        return s
#Runtime: 60 ms, faster than 77.65% of Python3 online submissions for Best Time to Buy and Sell Stock II.
#Memory Usage: 13.8 MB, less than 90.24% of Python3 online submissions for Best Time to Buy and Sell Stock II.