# 32. Longest Valid Parentheses
# 栈的合理使用
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        nums=[]
        max=-1
        i=0
        while i<len(s):
            if len(stack)==0:
                if s[i]==')':
                    nums=[]
                    i+=1
                    continue
            if s[i]=='(':
                stack.append(s[i])
                if len(stack)>len(nums):
                    nums.append(i)
            else:
                if stack:
                    stack.pop()
                    
                    if i-nums[len(stack)]>max:
                        max=i-nums[len(stack)]
                        
                    if len(nums)-len(stack)==2:
                        nums.pop()
            i+=1
        return max+1


# Runtime: 64 ms, faster than 25.37% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14 MB, less than 11.17% of Python3 online submissions for Longest Valid Parentheses