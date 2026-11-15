class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            '(': ')', '[': ']', '{': '}'
        }
        
        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if not stack or c != parentheses[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0