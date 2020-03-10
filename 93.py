#93. Restore IP Addresses
#递归刨去特殊情况
class Solution:
    def restoreIpAddresses(self, s: str):
        resl=[]
        res=""
        self.res,self.resl=res,resl
        self.deal(0,s)
        return self.resl
    def deal(self,n,s):
        st=""
        if n==4:
            if s=="":
                self.resl.append(self.res[:-1])
            return
        if s=="":
            return
        if s[0]=="0":
            self.res+="0."
            self.deal(n+1,s[1:])
            self.res=self.res[:-2]
        else:
            for i in range(min(len(s),3)):
                st+=s[i]
                if int(st)<=255:
                    self.res+=st+"."
                    self.deal(n+1,s[i+1:])
                    self.res=self.res[:-(i+2)]
                else:
                    break



sol=Solution()
sol.restoreIpAddresses("1111")
#Runtime: 36 ms, faster than 91.37% of Python3 online submissions for Restore IP Addresses.
#Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions for Restore IP Addresses.