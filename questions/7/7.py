class Solution:
    def reverse(self, x: int) -> int:
        
        #s = str(x)[::-1]
        if x >= 0 :
            s = int(str(x)[::-1])
        else:
            s = int("-"+str(x)[::-1][:-1])
            
        if abs(s).bit_length() >= 32:
            return 0
        return(s)
