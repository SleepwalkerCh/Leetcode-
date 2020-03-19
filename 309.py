#309. Best Time to Buy and Sell Stock with Cooldown
# 121题类似，感觉像有限状态自动机思路

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        buy,sell,cd=-prices[0],0,0
        for i in range(1,len(prices)):
            buy=max(buy,cd-prices[i])
            cd=max(cd,sell)
            sell=max(buy+prices[i],sell)
            res=max(sell,buy,cd)
        return res
#Runtime: 40 ms, faster than 54.77% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
#Memory Usage: 13.4 MB, less than 27.27% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.