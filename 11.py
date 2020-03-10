#11. Container With Most Water
#间距从大到小遍历，特殊数据会超时，改成cpp代码不会超时
leng=len(height)
result=-1
max1=-1
max2=-1
for i in range(leng):
    if height[i]>=max1:
        max2=max1
        max1=height[i]
    elif height[i]>=max2:
        max2=height[i]
for i in range(leng-1):
    width=leng-i-1
    maxpool=-1
    for j in range(leng-width):
        if height[j]<height[j+width]:
            pool=height[j]
        else:
            pool=height[j+width]
        if maxpool<pool*width:
            maxpool=pool*width
    if result<maxpool:
        result=maxpool
    if max2*width<=result:
        break
return result
            