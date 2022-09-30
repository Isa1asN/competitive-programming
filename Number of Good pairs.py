class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        counts = {}
        for num in nums:
            prior_num_count = counts.get(num, 0)
            pairs += prior_num_count
            counts[num] = prior_num_count + 1
        return pairs
