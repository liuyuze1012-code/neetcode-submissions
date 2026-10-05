class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = len(points)
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            heap.append([distance, x, y])

        heapq.heapify(heap)

        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res

