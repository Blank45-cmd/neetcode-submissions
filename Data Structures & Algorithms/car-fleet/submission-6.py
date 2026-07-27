class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack =[]
        for pos,spd in cars:
            time = ((target-pos)/spd)
            if not stack:
                stack.append(time)
            elif stack[-1]<time:
                stack.append(time)
            else:
                pass
        return len(stack)