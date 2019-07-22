class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        try :
            res = haystack.index(needle)
            return res
        except:
            return -1


## One-liner, built-in tools as well
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
	return haystack.find(needle)


## Brute-ish force
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

## First algorithmic step
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    i += j
                    break
                if j == len(needle)-1:
                    return i
        return -1
        
        

