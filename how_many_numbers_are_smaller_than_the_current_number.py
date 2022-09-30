class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        for i in nums:
            count= 0
            for j in nums:
                if i > j:
                    count+=1
            list.append(count)
        return list
e = Solution()
print(e.smallerNumbersThanCurrent([6,5,4,8]))
                
                
        
        
        
# Input: nums = [6,5,4,8]
#Output: [2,1,0,3]
