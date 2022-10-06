class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        
        for index, char in enumerate(s):
            if char.isdigit():
                num = 10 * num + int(char)
            if (not char.isdigit() and not char.isspace()) or index == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = char
                num = 0
        
        return sum(stack)
