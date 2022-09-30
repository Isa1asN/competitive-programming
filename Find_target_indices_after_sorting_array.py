class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        l = list(nums)
        l.sort()
        if l.count(target) == 1:
            temp.append(l.index(target))
        else:
            for i in range(l.count(target)):
                temp.append(l.index(target) + i)
                
        
        return temp
        
e = Solution()
print(e.targetIndices([1,2,5,2,3],3))
        
        
