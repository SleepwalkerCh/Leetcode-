#13. Roman to Integer
#字符串匹配方法解决问题
class Solution:
    def searchN(self,n:str,string:str) -> int:
        patt=re.compile(n)
        result = patt.findall(string)
        return len(result)
    def romanToInt(self, s: str) -> int:
        n_1=self.searchN('I',s)
        n_5=self.searchN('V',s)
        n_4=self.searchN('IV',s)
        n_9=self.searchN('IX',s)
        n_10=self.searchN('X',s)
        n_50=self.searchN('L',s)
        n_40=self.searchN('XL',s)
        n_90=self.searchN('XC',s)
        n_100=self.searchN('C',s)
        n_500=self.searchN('D',s)
        n_1000=self.searchN('M',s)
        n_400=self.searchN('CD',s)
        n_900=self.searchN('CM',s)
        return (n_1000-n_900)*1000+n_900*900+(n_500-n_400)*500+n_400*400+(n_100-n_400-n_900-n_90)*100+n_90*90+(n_50-n_40)*50+n_40*40+(n_10-n_9-n_40-n_90)*10+n_9*9+(n_5-n_4)*5+n_4*4+(n_1-n_4-n_9)