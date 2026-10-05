class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        heap = []
        for num in map.keys():
            heapq.heappush(heap, (map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res




#intuition:
#we build a hashmap that uses num as key and frequenceis as value
#then we push them into a heap
#pop things out of the min heap if the len(heap) > k
#then finally append the stuff in the heap to a result array


        