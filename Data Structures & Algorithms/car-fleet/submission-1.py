class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []

        for i in range(len(cars) - 1, -1, -1):
            pos, spd = cars[i]
            arrival = (target - pos) / spd
            if not stack or arrival > stack[-1]:
                stack.append(arrival)
        return len(stack)



    