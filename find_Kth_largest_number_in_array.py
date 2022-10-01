class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        tp = list(map(int, nums))
        tp.sort()
        return str(tp[::-1][k-1])
        
e = Solution()
print(e.kthLargestNumber(["3","6","7","10"],4))
