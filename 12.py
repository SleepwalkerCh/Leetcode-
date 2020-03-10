#12. Integer to Roman
#暴力解决
def intToRoman(self, num: int) -> str:
        st=""
        while num!=0:
            if num>=1000:
                num-=1000
                st+="M"
                continue
            if num>=900:
                num-=900
                st+="CM"
                continue
            if num>=500:
                num-=500
                st+="D"
                continue
            if num>=400:
                num-=400
                st+="CD"
                continue
            if num>=100:
                num-=100
                st+="C"
                continue
            if num>=90:
                num-=90
                st+="XC"
                continue
            if num>=50:
                num-=50
                st+="L"
                continue
            if num>=40:
                num-=40
                st+="XL"
                continue
            if num>=10:
                num-=10
                st+="X"
                continue
            if num>=9:
                num-=9
                st+="IX"
                continue
            if num>=5:
                num-=5
                st+="V"
                continue
            if num>=4:
                num-=4
                st+="IV"
                continue
            if num>=1:
                num-=1
                st+="I"
                continue
        return st