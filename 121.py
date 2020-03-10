#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        res,minnum,maxnum=0,prices[0],0
        for i in prices:
            if i<minnum:
                minnum=i
                maxnum=0
            if i>maxnum:
                maxnum=i
                res=maxnum-minnum
        return res
#Runtime: 52 ms, faster than 98.82% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 13.9 MB, less than 72.41% of Python3 online submissions for Best Time to Buy and Sell Stock.
