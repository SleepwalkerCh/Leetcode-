#22.Generate Parentheses
#递归生成满足条件的左括号序列
class Solution:
    def setLeft(self,now: int,n: int,l :List,result:List):
        if now>n:
            result_1=""
            for i in range(2*n):
                if i in l:
                    result_1+='('
                else:
                    result_1+=')'
            result.append(result_1)
        else:
            for i in range(l[-1]+1,2*n-1):
                if i<=(now-1)*2:
                    l.append(i)
                    self.setLeft(now+1,n,l,result)
                    l.pop()
                else: 
                    break
    def generateParenthesis(self, n: int) -> List[str]:
        list_l=[0]
        result=[]
        self.setLeft(2,n,list_l,result)
        return result

#Runtime: 44 ms, faster than 54.62% of Python3 online submissions for Generate Parentheses.
#Memory Usage: 13.3 MB, less than 66.73% of Python3 online submissions for Generate Parentheses
#1 10
#2 1010   
#  1100
#3 ["111000","110100","110010","101100","101010"]
#4 ["11110000","11101000","11100100","11100010","11011000","11010100","11010010","11001100","11001010","10111000","10110100","10110010","10101100","10101010"]
#1 2 5 14 42  132 429
#
#5 ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]
#