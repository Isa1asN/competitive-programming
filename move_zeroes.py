class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        
        """
        for i in nums:
            if i == 0:
                nums.pop(nums.index(i))
                nums.append(i)
        return nums
        
        
e = Solution()
print(e.moveZeroes([0]))
