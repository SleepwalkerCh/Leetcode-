#119. Pascal's Triangle II
# 数学方法

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        up,down=1,1
        num=[]
        for i in range((rowIndex)//2+1):
            num.append(up//down)
            up*=rowIndex-i
            down*=i+1
        if rowIndex%2==0:
            i=len(num)-2
        else:
            i=len(num)-1
        while i>=0:
            num.append(num[i])
            i-=1
        return num
#Runtime: 28 ms, faster than 70.12% of Python3 online submissions for Pascal's Triangle II.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle II.