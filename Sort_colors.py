class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []
        
        for i in nums :
            if i == 0:
                red.append(i)
            elif i==1:
                white.append(i)
            else:
                blue.append(i)
        nums[:] = red + white + blue
                
                
e = Solution()
print(e.sortColors([2,0,2,1,1,0]))
