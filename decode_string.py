class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[1, '']]
        for i, c in enumerate(s):
            if c.isdigit():
                if i == 0 or not s[i-1].isdigit():
                    stack.append([int(c), ''])
                else:
                    stack[-1][0] *= 10
                    stack[-1][0] += int(c)
            elif c not in ['[', ']']:
                stack[-1][1] += c
            elif c == ']':
                num, decoded = stack.pop()
                stack[-1][1] += decoded * num
        return stack[-1][1]
