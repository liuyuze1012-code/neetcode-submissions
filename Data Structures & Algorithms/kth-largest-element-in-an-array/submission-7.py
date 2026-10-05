class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        #nums = [1, 2, 3, 4, 5, 6]

        while len(nums) > k:
            heapq.heappop(nums)

        #nums = [4, 5]
        
        return nums[0]


