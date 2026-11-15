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

                # handles when extra bracket has no match
                if len(stack) == 0:
                    return False

                # find if closed bracket matches end of stack
                if pairs[c] == stack[-1]:
                    stack.pop() # remove from stack
                else:
                    return False # no match -> return False
        
        # if the stack length is zero by this point, we have checked       everything and can return True
        return len(stack) == 0
    

