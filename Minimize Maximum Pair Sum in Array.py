class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = deque(nums)
        mx = []
        while nums:
            mx.append(nums.popleft()+nums.pop())
        return max(mx[:])
        
