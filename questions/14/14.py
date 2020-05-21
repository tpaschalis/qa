## ## 
#["flower","flow","flight"]
#["aa","a"]
#["c","c"]
#[""]
## ## 

# Try 1/2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        if len(strs) == 0 :
            return prefix
        
        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix, 0):
            #while s[:len(prefix)].find(prefix) == -1:
                prefix = prefix[:-1]
        
        return prefix

# Runtime: 36 ms, faster than 82.95% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.1 MB, less than 86.31% of Python3 online submissions for Longest Common Prefix.
# Runtime: 32 ms, faster than 94.91% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Longest Common Prefix.
# Runtime: 32 ms, faster than 94.91% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.1 MB, less than 85.61% of Python3 online submissions for Longest Common Prefix.
# Runtime: 32 ms, faster than 94.91% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 17.84% of Python3 online submissions for Longest Common Prefix.


# Try 3
# Vertical Scanning

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        res = ""
        if len(strs) == 0 or strs[0] == "":
            return prefix
        
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            j = 1
            while j < len(strs):
                if i == len(strs[j]) or strs[j][i] != c :
                    return strs[0][:i]
                j += 1
            i += 1

        return strs[0]      # This is the secret sauce

# Runtime: 40 ms, faster than 53.50% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.2 MB, less than 60.21% of Python3 online submissions for Longest Common Prefix.
# Runtime: 36 ms, faster than 82.95% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 17.84% of Python3 online submissions for Longest Common Prefix.
# Runtime: 52 ms, faster than 12.94% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.5 MB, less than 5.11% of Python3 online submissions for Longest Common Prefix.


# Try 4
# Using zip/set

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        res = ""

        strzip, res = zip(*strs), ""
        
        for s in strzip:
            # s
            #('f', 'f', 'f')
            #('l', 'l', 'l')
            #('o', 'o', 'i')
            print(s)
            if len(set(s)) > 1 :
                break
            res = res + s[0]
        return res

# Runtime: 32 ms, faster than 94.91% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.2 MB, less than 48.61% of Python3 online submissions for Longest Common Prefix.
# Runtime: 36 ms, faster than 82.95% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 27.87% of Python3 online submissions for Longest Common Prefix.
# Runtime: 40 ms, faster than 53.50% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.2 MB, less than 58.85% of Python3 online submissions for Longest Common Prefix.


# Try 5
# Divide and Conquer, recursively

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0 or strs == [""]:
            return ""

        def divide(strs: List[str], l:int, r:int) :
            if l == r :
                return strs[l]
            else :
                mid = int((l+r)/2)
                lcp_left = divide(strs, l, mid)
                lcp_right = divide(strs, mid+1 ,r)
                return conquer(lcp_left, lcp_right)

        def conquer(lstr: str, rstr: str) -> str:
            minimum = min(len(lstr), len(rstr))
            for i in range(minimum):
                if lstr[i] != rstr[i] :
                    return lstr[:i]
            return lstr[:minimum]



        return divide(strs, 0, len(strs)-1)

# Runtime: 40 ms, faster than 53.50% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Longest Common Prefix.
# Runtime: 52 ms, faster than 12.94% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 19.04% of Python3 online submissions for Longest Common Prefix.
# Runtime: 36 ms, faster than 82.95% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.2 MB, less than 63.58% of Python3 online submissions for Longest Common Prefix.
# Runtime: 40 ms, faster than 53.50% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.4 MB, less than 14.75% of Python3 online submissions for Longest Common Prefix.


# Try 6
# Binary Search, recursive

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0 :
            return ""
        
        def is_common_prefix(strs: List[str], length: int):
            w = strs[0][:length]
            for i in range(1, len(strs)):
                if not strs[i].startswith(w):
                    return False
            return True
            
            
        min_len = 2**30
        
        for s in strs:
            min_len = min(min_len, len(s))
            
        low, high = 1, min_len
        
        while low <= high:
            middle = int((low + high)/2)
            if is_common_prefix(strs, middle): 
                low = middle + 1
            else :
                high = middle - 1

        fin = int((low+high)/2)
        return strs[0][:fin]
        

# Runtime: 28 ms, faster than 99.11% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 31.04% of Python3 online submissions for Longest Common Prefix.
# Runtime: 52 ms, faster than 12.94% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.1 MB, less than 86.31% of Python3 online submissions for Longest Common Prefix.
# Runtime: 32 ms, faster than 94.91% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 31.04% of Python3 online submissions for Longest Common Prefix.
# Runtime: 28 ms, faster than 99.11% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 44.13% of Python3 online submissions for Longest Common Prefix.
