class Solution(object):
    def minSetSize(self, arr):
        count = Counter(arr)
        currentCount = 0
        currentSize = 0
        for value in sorted(count.values(), key=None, reverse=True):
            currentSize += 1
            if currentCount + value >= len(arr) // 2:
                return currentSize
            currentCount += value
        
        