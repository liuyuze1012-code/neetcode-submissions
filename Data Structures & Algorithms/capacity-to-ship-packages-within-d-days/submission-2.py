class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canShip(cap):
            ships = 1
            load = 0
            for w in weights:
                if load + w > cap:
                    ships += 1
                    load = 0
                load += w
           
            return ships <= days



        while l <= r:
            m = (l + r)//2
            if canShip(m):
                r = m - 1
            else:
                l = m + 1
        
        return l





#create a fucntion that determine whether x day can shipwithin days
#and use binary search and check if it can ship within days, and the upper bound is the largest value in weights




