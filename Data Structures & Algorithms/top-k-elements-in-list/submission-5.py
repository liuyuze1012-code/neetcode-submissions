class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        #[1, 1, 1, 3, 3, 4, 4, 4, 4, 4] k = 2
        #{1:3; 3:2; 4:5}
        heap = []
        for num in map.keys():
            heapq.heappush(heap, (map[num], num))
            #heap = [(5, 4), (3, 1), (2, 3)]
            while len(heap) > k:
                heapq.heappop(heap)
                #heap = [(5, 4), (3, 1)]
        
        res = []
        for i in range(k):
            res.append(heap[i][1])
        
        return res