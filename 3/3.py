class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        d = dict()
        res = 0
        while j < len(s):
            if s[j] in d.keys():
                i = max(i, d[s[j]])
            res = max(res, j - i + 1)
            d[s[j]] = j + 1
            j = j + 1
        return res
