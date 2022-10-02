class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))]
        stk = []
     
        for i in range(len(temperatures)):
            if len(stk)==0 or temperatures[i]<=temperatures[stk[-1]]:
                stk.append(i)
            else:
                while stk and temperatures[i] > temperatures[stk[-1]]:
                    idx = stk.pop()
                    ans[idx] = i-idx
                stk.append(i)
        return ans
