#  122. Best Time to Buy and Sell Stock II
#  找到极值点
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s,i=0,0
        small=-1
        if len(prices)<=1:
            return 0
        for i in range(len(prices)):
            if i==0:
                if prices[1]>=prices[0]:
                    small=prices[0]
                continue
            if i==len(prices)-1:
                
                if prices[len(prices)-1]>=prices[len(prices)-2]:
                    if small!=-1:
                        s+=prices[len(prices)-1]-small
                continue
            if (prices[i]<prices[i+1] and prices[i]<=prices[i-1]) or (prices[i]<=prices[i+1] and prices[i]<prices[i-1]):
                small=prices[i]
                continue
            if (prices[i]>prices[i+1] and prices[i]>=prices[i-1]) or (prices[i]>=prices[i+1] and prices[i]>prices[i-1]):
                if small!=-1:
                    s+=prices[i]-small
                    small=-1
                    continue
        return s
#Runtime: 76 ms, faster than 12.27% of Python3 online submissions for Best Time to Buy and Sell Stock II.
#Memory Usage: 14.1 MB, less than 7.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.