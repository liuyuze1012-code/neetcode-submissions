class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * 2*n
        for i, num in enumerate(nums):
            result[i] = result[i + n] = num

        return result
