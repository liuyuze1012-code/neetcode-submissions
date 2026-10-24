class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in nums:
            list1.append(i)
        
        ans = []
        ans = list1 + nums
        return ans