class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        max_num = 0
        res = 0
        for num in nums:
            map[num] += 1
            if max_num < map[num]:
                res = num
                max_num = map[num]
        return res

        