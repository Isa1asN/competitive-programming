class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = ret = 0
        window_sum = 0
        while right < len(nums):
            # maintain the invariant that k is enough to
            # change all elements between left and right
            # inclusively to nums[right]
            window_sum += nums[right]
            while nums[right]*(right-left+1)-window_sum > k:
                window_sum -= nums[left]
                left += 1
            ret = max(ret, right-left+1)
            right += 1
        return ret
