# Cheat no1
class Solution:
    myPow = pow

# Cheat no2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

# Iteratively

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            res = res * x
        return res if n >= 0 else 1./res   


# O(logn) recursively
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0 :
            return 1
        
        if n < 0 :
            return 1 / self.myPow(x, -n)
        
        if n % 2 == 1:
            return self.myPow(x, n-1) * x
        
        return self.myPow(x*x, n/2)

# O(logn) iteratively
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0 :
            return 1
        m = abs(n)
            
        exp = 1
        while m != 0:
            if m % 2 == 1:
                exp = exp * x
            x = x * x
            m >>= 1
            
        return exp if n > 0 else 1./exp


# More concise O(logn) iteratively

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 1:
            return x
        if n == -1 :
            return 1. / x
        if n == 0 :
            return 1.0

        half = self.myPow(x, n / 2);
        return half * half * self.myPow(x, n % 2);
