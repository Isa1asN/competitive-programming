class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        i=1
        num=[]
        
        while i<len(nums):
            if nums[i]<=nums[i-1]:
                c+=(nums[i-1]-nums[i]+1)
                nums[i]=nums[i-1]+1
            i+=1
        return c
    
