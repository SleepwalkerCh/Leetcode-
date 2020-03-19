# 150. Evaluate Reverse Polish Notation
# 使用栈计算表达式
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num=0
        stack=[]
        exp=["+","-","*","/"]
        for i in tokens:
            if i in exp:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    res=a+b
                elif i=="-":
                    res=a-b
                elif i=="*":
                    res=a*b
                else:
                    res=maths.trunc(a/b)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[-1]
#Runtime: 72 ms, faster than 33.24% of Python3 online submissions for Evaluate Reverse Polish Notation.
#Memory Usage: 13.4 MB, less than 26.09% of Python3 online submissions for Evaluate Reverse Polish Notation.