class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack maintains our working list of unresolved temps
        # push as we iterate; pop when we get our answer
        
        stack = []
        output = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                earlyday = stack.pop()
                output[earlyday] = day - earlyday
            stack.append(day)

        return output
