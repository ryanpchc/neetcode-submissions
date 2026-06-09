class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{',}

        for bracket in s:
            # if open bracket
            if bracket not in pairs:
                stack.append(bracket)

            # if closed bracket
            else:
                if len(stack) != 0:
                    if stack[-1] == pairs[bracket]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0