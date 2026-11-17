class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] 

        for i, temp in enumerate(temperatures):

            # while stack exists & current temp hotter than temp stored in stack
            while stack and temp > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i - previous_index 
        
            stack.append(i) # push today's index

        return result
            