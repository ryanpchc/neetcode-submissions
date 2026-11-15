class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parentheses = ['(', '{', '[']
        parentheses = {
            ')': '(', 
            '}': '{',
            ']': '['
        }
        
        for c in s:

            if c in open_parentheses:
                stack.append(c)
            else:
                if stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0