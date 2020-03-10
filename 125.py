# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if (i<='z' and i>='a') or (i<='Z' and i>='A') or (i<='9' and i>='0'):
                st+=i
        st=st.lower()
        i,j = 0,len(st)-1
        while i<j:
            if st[i]!=st[j]:
                return False
            i+=1
            j-=1
        return True
#Runtime: 48 ms, faster than 61.17% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 13.2 MB, less than 94.05% of Python3 online submissions for Valid Palindrome.