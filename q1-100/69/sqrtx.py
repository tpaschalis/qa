class Solution:
    def mySqrt(self, x: int) -> int:
        
        new_guess, old_guess, x = 1, float(x), float(x)
        if x == 0:
            return 0

        while abs(new_guess - old_guess) > 0.5:
            old_guess = new_guess
            new_guess = 0.5 * (old_guess + x / old_guess)
            
        
        return int(new_guess)


class Solution:
    def mySqrt(self, x: int) -> int:
        
        return int(x**(1/2))
