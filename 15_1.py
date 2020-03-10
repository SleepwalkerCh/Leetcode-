#15 3Sum
# 抓两个找一个，用if 解决特殊情况 很慢
nums=[0,0,0]
numset=set(nums)
numlist=list(numset)
result=[]
for i in range(len(numlist)):
    for j in range(i,len(numlist)):
        print(i,j)
        if (-numlist[i]-numlist[j]) in numset:
            if numlist[i]==numlist[j]:
                if nums.count(numlist[i])<=1:
                    continue
            if -numlist[i]-numlist[j]==numlist[i]:
                if nums.count(numlist[i])<=1:
                    continue
            if -numlist[i]-numlist[j]==numlist[j]:
                if nums.count(numlist[j])<=1:
                    continue
            if (numlist[i]==0) and (numlist[j]==0):
                if nums.count(0)<=2:
                    continue
            if numlist.index(-numlist[i]-numlist[j])>=j:
                result.append([numlist[i],numlist[j],-numlist[i]-numlist[j]])
print(result)