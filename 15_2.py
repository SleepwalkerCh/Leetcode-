#15 3Sum
#对数列进行排序，固定一个数字之后，后两位逐渐逼近寻找target
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break           #之后 的优化部分
            if i!=0 and nums[i]==nums[i-1]:
                continue
            else:
                j=i+1
                k=len(nums)-1
                while j<k:
                    if nums[j]+nums[k]+nums[i]==0:
                        result.append([nums[i],nums[j],nums[k]])
                        k-=1
                        j+=1
                        while nums[j-1]==nums[j] and j<k:
                            j+=1
                        while nums[k+1]==nums[k] and j<k:
                            k-=1
                    elif nums[j]+nums[k]+nums[i]<0:
                        j+=1
                        while nums[j-1]==nums[j]:
                            j+=1
                    else:
                        k-=1
                        while nums[k+1]==nums[k]:
                            k-=1
                    
        return result                
#Runtime: 1620 ms, faster than 16.11% of Python3 online submissions for 3Sum.
#Memory Usage: 16.7 MB, less than 74.40% of Python3 online submissions for 3Sum                   
#添加第8,9行加快了运行速度
#Runtime: 1300 ms, faster than 26.31% of Python3 online submissions for 3Sum.
#Memory Usage: 16.9 MB, less than 39.54% of Python3 online submissions for 3Sum.
# 1,2,25,48,50
