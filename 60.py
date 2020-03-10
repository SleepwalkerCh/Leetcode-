# 60. Permutation Sequence
#数学知识解决问题
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def Factorial(n):
            sum=1
            for i in range(n):
                sum=sum*(i+1)
            return sum
        res=""
        i=n
        num=[]
        k-=1
        for j in range(n):
            num.append(j+1)
        
        while i>=1:
            P=Factorial(i-1)
            if k==0:
                res+=str(num[0])
                del(num[0])
                i-=1
                continue
            for j in range(len(num)):
                if j*P>=k:
                    break
            print(k,j,P,len(num))
            if k<j*P:
                j-=1
            k-=j*P
            
            res+=str(num[j])
            del(num[j])
            i-=1
        return res
            



#Runtime: 36 ms, faster than 72.38% of Python3 online submissions for Permutation Sequence.
#Memory Usage: 14 MB, less than 5.23% of Python3 online submissions for Permutation Sequence.


