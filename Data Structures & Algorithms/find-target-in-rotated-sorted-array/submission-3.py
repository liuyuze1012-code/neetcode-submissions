class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min(nums):
            n = len(nums)
            l = 0
            r = n - 1
            while l < r:
                m = (l + r)//2

                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            
            return l
        
        n = len(nums)
        l = 0
        r = n - 1
        min_index = find_min(nums)
        # checking if the array is the same after rotated
        if min_index == 0:
            l, r = 0, n - 1
        # checking if target is in the left partition
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l = 0
            r = min_index - 1
        # checking if target is in the right partition
        elif target >= nums[min_index] and target <= nums[n - 1]:
            l = min_index
            r = n - 1

        # conduct traditional binary search
        while l <= r:
            m = (l + r)//2

            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1

                    




# 3  4  5  6  1  2
#          l  m
#                r

# first find the min_index using binary search
# after findning the min_index
# if target > nums[min_index], we do binary search from nums[0:min_index]
# if target < nums[min_index], we do binary search from nums[min_index:n]
# if min_index = 0, binary search from nums[0:n] 