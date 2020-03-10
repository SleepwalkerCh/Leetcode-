#96. Unique Binary Search Trees
#直接求95list的长度会超时 递归方法
class Solution:
    def numTrees(self, n: int) -> int:
        return self.calc(n)
    def calc(self,n:int):
        if n<2:
            return 1
        else:
            sum=0
            for i in range(n):
                if n-1-i<=i:
                    break
                sum+=self.calc(n-1-i)*self.calc(i)
            sum*=2
            
            if n%2!=0:
                sum+=self.calc((n-1)//2)**2
            return sum
#Runtime: 276 ms, faster than 7.51% of Python3 online submissions for Unique Binary Search Trees.
#Memory Usage: 13.9 MB, less than 10.71% of Python3 online submissions for Unique Binary Search Trees.
0 1
1 1
2 2=1+1
3 5=2+1+2
4 14=5+1*2+1*2+5
5 42 = 14+5+2*2+5+14
6 132 
7 429