#56. Merge Intervals
# 需要排序，好像有点慢

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        res.append()

        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda t:t[0])
        i=1
        minrange,maxrange=intervals[0][0],intervals[0][1]
        while i<len(intervals):
            if maxrange>=intervals[i][0]:
                maxrange=intervals[i][1]
                
            else:
                res.append([minrange,maxrange])
                
                if i==len(intervals):
                    break
                minrange,maxrange=intervals[i][0],intervals[i][1]
            i+=1
        res.append([minrange,maxrange])
        return res
#Runtime: 92 ms, faster than 5.32% of Python3 online submissions for Merge Intervals.
#Memory Usage: 15.7 MB, less than 23.11% of Python3 online submissions for Merge Intervals.