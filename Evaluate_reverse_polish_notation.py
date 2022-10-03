class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s =='+':
                stack.append(int(stack.pop())+(int(stack.pop())))
            elif s =='-':
                val1,val2=stack.pop(),stack.pop()
                stack.append(int(val2)-(int(val1)))
            elif s =='*':
                stack.append(int(stack.pop())*(int(stack.pop())))
            elif s =='/':
                val1,val2=stack.pop(),stack.pop()
                stack.append(int(val2)/(int(val1)))
            else:
                stack.append(s)
        return int(stack.pop())
        
