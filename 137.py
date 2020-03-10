#137. Single Number II
# 正负数分开处理
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def XOR3(a,b)->int:
            num,power=0,1
            if a<b:
                temp=a
                a=b
                b=temp
            while a!=0 and b!=0:
                num+=(a%3+b%3)%3*power
                power*=3
                a,b=a//3,b//3
            while a!=0:
                num+=a%3*power
                power*=3
                a=a//3
            return num
        num1,num2=0,0
        for i in nums:
            if i>0:
                num1=XOR3(num1,i)
            if i<0:
                num2=XOR3(num2,-i)
        if num1!=0:
            return num1
        else:
            return -num2
        
#Runtime: 148 ms, faster than 10.14% of Python3 online submissions for Single Number II.
#Memory Usage: 14.2 MB, less than 80.00% of Python3 online submissions for Single Number II.