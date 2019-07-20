class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        # "The divisor will never be 0."
        #if d2 == 0:
            #return 2**31 -1
    
        is_positive = (dividend < 0) == (divisor < 0)
        res = math.log(abs(dividend)) - math.log(abs(divisor))
        res = int(math.exp(res))
        if is_positive:
            return min(res, 2147483647)
        return max(0-res, -2147483648)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        positive = (dividend < 0) is (divisor < 0)

        dividend, divisor, res = abs(dividend), abs(divisor), 0

        while dividend >= divisor:
            
            n1, n2 = 1, divisor
            
            while dividend >= n2:
                dividend, res = dividend - n2, res + n1
                n1, n2 = n1<<1, n2<<1
        
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
