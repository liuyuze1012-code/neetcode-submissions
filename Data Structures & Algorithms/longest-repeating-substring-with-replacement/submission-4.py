class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            # creating a hashmap that maps each ch to freq
            count[s[r]] = 1 + count.get(s[r], 0)
            # finding the max freq in the map
            maxf = max(maxf, count[s[r]])

            # if length of current window - maxf < k
            # this means we need to shrink
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)

        return res
        




# sliding window
# dynamic window
# A A A B A B B
# l           r
# create a hashmap where keys are characters and fequencies are values
# while we loop through s
# {A: 3, B: 1}
# if current window size - max frequency in the map is smaller than k
# then the window is valid
# if not valid
# we shrink the window size by 1 and adjust counts
# find the max length
