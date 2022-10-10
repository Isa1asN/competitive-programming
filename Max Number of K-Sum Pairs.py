class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        l=0
        r=len(nums)-1
        cnt=0
        while l<r:
            sumi=nums[l]+nums[r]
            if sumi==k:
                cnt+=1
                l+=1
                r-=1
            elif sumi>k:
                r-=1
            else:
                l+=1
        return cnt

