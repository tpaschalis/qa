# 9. Palindrome Number

Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

### Examples
Example 1:
```
Input: 121
Output: true
```

Example 2:
```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

Example 3:
```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

Follow up:

Coud you solve it without converting the integer to a string?


### Testcases
```
0
10
11
121
12345654321
123454321

# expected
# true
# false
# true
# true
# false (overflow)
# true
```

### Benchmarks and Remarks

```
 Runtime: 68 ms, faster than 82.28% of Python3 online submissions for Palindrome Number.
 Memory Usage: 13.3 MB, less than 43.24% of Python3 online submissions for Palindrome Number.
```

I tried to solve the problem *without* converting the number to an integer, where more advanced algorithms could have been used.

The main strategy is to take the initial number, take digits off its 'tail' and add them to the result 'head'.

In the end, if the two numbers are equivalent, the initial input is a palindrome.

To make it more efficient, and having discarded some edge cases, we only need to 'flip' at least half the number, and then compare it to the original.
