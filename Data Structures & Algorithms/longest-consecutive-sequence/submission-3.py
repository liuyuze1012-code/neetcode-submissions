class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                next_num = num + 1
                while next_num in numSet:
                    length += 1
                    next_num += 1
                longest = max(length, longest)
        return longest