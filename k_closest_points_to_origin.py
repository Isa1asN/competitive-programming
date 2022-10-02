class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        t=[]
        for i in points:
            x=i[0]**2+i[1]**2
            t.append([x,i])
        t.sort()
        return([i[1] for i in t[:k]])
        

e = Solution()
print(e.kClosest([[3,3],[5,-1],[-2,4]],2))
