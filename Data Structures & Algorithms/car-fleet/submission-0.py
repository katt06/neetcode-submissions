class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #this is a monotonic stack: result array, for lopp, while loop, stack.pop, and stack.append are needed (check this requirement)
        
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        #reversing [start, end, increment]
        for p, s in sorted(pairs)[::-1]:
        #equation is target-position / speed
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        #return the # of diff car fleets 
        return len(stack)
        