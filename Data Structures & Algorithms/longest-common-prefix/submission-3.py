class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #idea is that we conduct a vertical scan
        #use the first word in strs as an anchor
        #loop through each character for each str one by one
        #if we see a difference then we return everything up until i
        #edge case 1: length runs out, so if i = len(s)
        #edge case 2: empty string or an empty character ["a"]

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
            
        return strs[0]