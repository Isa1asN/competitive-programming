class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i],speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        # using stack to capture unique number of fleets
        stk = []
        ans = 0
        for pos,spd in arr:
            curr = (target-pos)/spd
            # when stk is empty or car at back is slower than car at front then it will become a new fleet
            if len(stk)==0 or curr > stk[-1]:
                stk.append(curr)
                ans+=1
           # there is no need to handle else case, if car at back is faster they become part of the fleet, 
           # hence no need to insert.
            
        return ans
