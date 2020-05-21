class Solution:
    def myAtoi(self, str: str) -> int:
        sign = {"-", "+"}
        res = 0

        str = str.strip()
        if str == "":
            return 0

        kind = -1 if str[0] == "-" else 1
        if str[0] in sign: 
            str = str[1:]
        
        for i, c in enumerate(str):
            if not c.isdigit(): 
                break
            res = res*10 + int(c)
            
        return max(-2**31, min(kind * res,2**31-1))                



class Solution:
    def myAtoi(self, str: str) -> int:
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        sign = {"-", "+"}
        res = 0
        kind = +1
        s = ""
        
        for i, c in enumerate(str):
            if c != ' ':
                str = str[i:]
                break
        
        if str == "":
            return 0
        # We have to deal with silly input like "-+1" and "+-2"
        kind = -1 if str[0] == "-" else 1
        if str[0] in sign:
            str = str[1:]
        
        for i, c in enumerate(str):
            if c not in digits:
                break
            res = res*10 + int(c)
            
        if res.bit_length() >= 32:
            if kind > 0 :
                return 2 ** 31 -1 
            else :
                return -2**31
        return res * kind
                
            
