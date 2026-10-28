class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1
            window.add(s[i])
            res = max(res, i - l + 1)
                   
        return res

# window = set(y, z, x)
# z  x  y  z  x  y  z
#             i
#       l
# window = (w, k, e)
# length = 2
# max_length = 2
# p w w k e w
#         i
#     l
