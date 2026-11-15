class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        matches = {
            ')': '(', 
            '}': '{', 
            ']': '[',
        }

        for c in s:
            # if open, append to stack
            if c in open_brackets:
                stack.append(c)

            # for all closed brackets
            else:
                if not stack:
                    return False
                
                if matches[c] != stack[-1]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0