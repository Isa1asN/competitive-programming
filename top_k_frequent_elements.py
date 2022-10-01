class Solution(object):
    def topKFrequent(self, nums, k):
        result = []
        dict = collections.Counter(nums)
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        for key, value in dict[:k]:
            result.append(key)
        return result
                
            
