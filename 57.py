# 57. Insert Interval
# 
class Solution:
    def insert(self, intervals, newInterval):
        i=0
        while i<len(intervals):
            if intervals[i][0]>=newInterval[0]:
                break
            i+=1
       
        flag1=i
        if flag1==0:
            start=newInterval[0]
        elif flag1==len(intervals) and intervals[flag1-1][1]<newInterval[0]:
            start=newInterval[0]
            
        elif intervals[flag1-1][1]>=newInterval[0]:
            start=intervals[flag1-1][0]
            flag1-=1
        else:
            start=newInterval[0]
        
        i=len(intervals)-1
        while i>=0:
            if intervals[i][1]<=newInterval[1]:
                break
            i-=1
        flag2=i

        if flag2==len(intervals)-1:
            end=newInterval[1]
        elif flag2==-1 and intervals[flag2+1][0]>newInterval[1]:
            end=newInterval[1]
        elif intervals[flag2+1][0]<=newInterval[1]:
            end=intervals[flag2+1][1]
            flag2+=1
        else:
            end=newInterval[1]
        res=[]
        for i in range(flag1):
            res.append(intervals[i])
        res.append([start,end])
        
        for i in range(flag2+1,len(intervals)):
            res.append(intervals[i])
        return res
    
sol=Solution()
print(sol.insert([[2,3],[6,9]],[3,11]))
#Runtime: 84 ms, faster than 5.66% of Python3 online submissions for Insert Interval.
#Memory Usage: 17.2 MB, less than 5.13% of Python3 online submissions for Insert Interval.