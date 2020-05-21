# 29. Divide Two Integers

Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

### Examples

Example 1:
```
Input: dividend = 10, divisor = 3
Output: 3
```

Example 2:
```
Input: dividend = 7, divisor = -3
Output: -2
```

Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


### Testcases
```
10
3
7
-3
0
5
```

### Benchmarks and Remarks

```
 Runtime: 32 ms, faster than 94.42% of Python3 online submissions for Divide Two Integers.
 Memory Usage: 13.8 MB, less than 5.37% of Python3 online submissions for Divide Two Integers.
 Runtime: 32 ms, faster than 94.42% of Python3 online submissions for Divide Two Integers.
 Memory Usage: 14.1 MB, less than 5.37% of Python3 online submissions for Divide Two Integers.
 Runtime: 40 ms, faster than 57.93% of Python3 online submissions for Divide Two Integers.
 Memory Usage: 14.1 MB, less than 5.37% of Python3 online submissions for Divide Two Integers.
```

Hmm, so we need to 'cheat' in a clever way, right? One could either use logarithms and exponentials to achieve the division (and then cast the result to `int`), or use bit-shifting as a makeshift "multiply by two", to achieve the same thing.
