class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        d = {'I': 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}
        
        i = 0
        while i < len(s) - 1:
            if d[s[i]] >= d[s[i+1]]:
                res += d[s[i]]
            else :
                res -= d[s[i]]
            i += 1
        res += d[s[len(s)-1]]
        return res

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        d = {'I': 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}
        
        i = 0
        for c in s:
            res += d[c]
            
        if "IV" in s :
            res -= 2
        if "IX" in s: 
            res -= 2
        if "XL" in s:
            res -= 20
        if "XC" in s:
            res -= 20
        if "CD" in s:
            res -= 200
        if "CM" in s:
            res -= 200
        
        return res
