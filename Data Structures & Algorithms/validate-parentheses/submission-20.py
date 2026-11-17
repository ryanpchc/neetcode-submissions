class Solution:
    def isValid(self, s: str) -> bool:
        # need a data structure that checks last in first out for open closed parentheses
        stack = []
        open_parentheses = ['(', '{', '[']
        parentheses = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }

        # iterate through string
        for c in s:
            # append c to stack if open parentheses
            if c in open_parentheses:
                stack.append(c)
            else:
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()

        return not stack