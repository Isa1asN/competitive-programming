class Solution:
    def checkArithmeticSubarrays(self, nums, l, r) :
        i = 0
        ans = []
        
        
        def is_arithmetic(l):
            delta = l[1] - l[0]
            for index in range(len(l) - 1):
                if not (l[index + 1] - l[index] == delta):
                     return False
            return True
        
        while i < len(l):
            temp = nums[l[i] : r[i]+1]
            temp.sort()
            
            ans.append(is_arithmetic(temp))
            
            i += 1
        return ans
            
                
            
e = Solution()
print(e.checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))
