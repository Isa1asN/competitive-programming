class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:return []
        changed.sort()
        c=Counter(changed)
        ans=[]
        if c[0]%2==0:
            ans+=[0]*(c[0]//2)
            
        for i in c:
            if i==0 or c[i]==0:
                continue
            elif (i*2 not in c) or c[i]>c[i*2]:
                return []
            c[i*2]-=c[i]
            ans+=[i]*c[i]
                
        return ans
