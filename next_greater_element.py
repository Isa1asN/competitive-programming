class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        d = {}
        
        for e in nums2:
            
            while(stack and e > stack[-1]):
                c = stack.pop()
                d[c] = e
            
            stack.append(e)
        
        return [d.get(e, -1) for e in nums1]
