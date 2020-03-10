#20. Valid Parentheses
#对栈的操作可简单解题
class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':1,'[':2,'{':3,')':4,']':5,'}':6}
        stack=[]
        for i in s:
            if d[i]<=3:
                stack.append(d[i])
            else:
                if not stack:
                    return False
                else:
                    if d[i]-3==stack[-1]:
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        else:
            return True
#Runtime: 32 ms, faster than 94.11% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 13.1 MB, less than 85.09% of Python3 online submissions for Valid Parentheses.
