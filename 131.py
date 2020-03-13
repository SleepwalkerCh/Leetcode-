#131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        flag=[]*len(s)
        for i in range(1,len(s)):
            for j in range(1,i):
                flag[j]