#  123. Best Time to Buy and Sell Stock III
#  用 121 题的思路，从前往后和从后往前的最优解决方法记录下来
# 时间复杂度O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        first,last = [],[]
        for i in prices:
            first.append(0)
            last.append(0)
        
        minnum,maxnum=prices[0],0
        for i in range(1,len(prices)):
            first[i]=first[i-1]
            if prices[i]<minnum:
                minnum=prices[i]
                maxnum=0
            if prices[i]>maxnum:
                maxnum=prices[i]
                if first[i-1]<maxnum-minnum:
                    first[i]=maxnum-minnum

        minnum,maxnum=-1,prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            last[i]=last[i+1]
            if prices[i]>maxnum:
                maxnum=prices[i]
                minnum=-1
            if prices[i]<minnum or minnum==-1:
                minnum=prices[i]
                if last[i]<maxnum-minnum:
                    last[i]=maxnum-minnum
        res=0
        for i in range(len(prices)):
            if res<last[i]+first[i]:
                res=last[i]+first[i]
        return res
#Runtime: 76 ms, faster than 79.59% of Python3 online submissions for Best Time to Buy and Sell Stock III.
#Memory Usage: 14.1 MB, less than 63.64% of Python3 online submissions for Best Time to Buy and Sell Stock III.