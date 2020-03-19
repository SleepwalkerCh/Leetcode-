#714. Best Time to Buy and Sell Stock with Transaction Fee
# 参照309,121
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)<2:
            return 0
        buy,sell,cd=-prices[0],0,0
        for i in range(1,len(prices)):
            buy=max(buy,sell-prices[i])
            
            sell=max(buy+prices[i]-fee,sell)
            res=max(sell,buy,cd)
        return res
#Runtime: 888 ms, faster than 28.95% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
#Memory Usage: 19.5 MB, less than 12.50% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.