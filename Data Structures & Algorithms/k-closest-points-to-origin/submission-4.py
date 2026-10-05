class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = len(points)
        for x, y in points:
            distance = (x * x) + (y * y)
            heap.append([distance, x, y])

        heapq.heapify(heap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1

        return res

