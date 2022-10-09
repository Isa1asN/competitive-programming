class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        j=len(nums)-1
        if j==0:
            return
        if j+1<k:
            k=k%(j+1)
        ans=[0 for i in range(len(nums))]
        for p in range(len(nums)):
            if k>0:
                ans[k-1]=nums[j]
                j-=1
                k-=1
            else:
                ans[p]=nums[i]
                i+=1
        for i in range(len(ans)):
            nums[i]=ans[i]
