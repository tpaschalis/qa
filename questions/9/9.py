class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Reversing will lead to stray negative or starting zero
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        
        res = 0
        
        while res < x: #  and  x > 0 :
            res =  (res * 10) + (x % 10)
            x = int(x/10)

        if res.bit_length() >= 32:
            return False
        
        return x == res or x == int(res/10)
