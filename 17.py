#17. Letter Combinations of a Phone Number
class Solution:
    self.a=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    def createlist(self,old: list,num: int)->List[str]:
        new=[]
        for i in old:
            for j in self.a[num-2]:
                new.append(i+j)
    def letterCombinations(self, digits: str) -> List[str]:
        
        result=[""]
        for i in digits:
            result=self.createlist(result,num)   
        return result
# Runtime: 36 ms, faster than 80.49% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.2 MB, less than 34.13% of Python3 online submissions for Letter Combinations of a Phone Number.