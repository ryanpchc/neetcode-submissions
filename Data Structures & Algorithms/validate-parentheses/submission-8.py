class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        pairs = {
            ')': '(', 
            '}': '{', 
            ']': '[',
        }

        for c in s:
            # if char is an open bracket
            if c not in pairs:
                stack.append(c)
            
            # else char is a closed bracket
            else:
                if len(stack) == 0:
                    return False

                if pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

