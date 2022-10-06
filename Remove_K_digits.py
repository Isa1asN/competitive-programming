class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while len(stack) and stack[-1] > d and k:
                stack.pop()
                k -= 1
            if len(stack) or d != '0':
                # equal to `if not(len(stack) == 0 and d == '0')`
                # not to append 0 at tail of the stack
                stack.append(d)
        if k :
            stack = stack[:-k]
        return ''.join(stack) if len(stack) else '0'
