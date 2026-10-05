class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

#speed = distance * time
#time = speed / distance
#if time_car1 <= time_car2, they become a fleet
#for p in position target - p and we devide that by speed, so we
#get the time for each

#target = 10, position = [4,1,0,7], speed = [2,2,1,1]

#time = [3, 4.5, 10, 3]
#fleet_count = 0
#a = 3
#time = [3, 4.5]
#a <= 10? no
#time = [3, 4.5]
#a <= 4.5? no
#time = [3]
