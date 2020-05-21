# 28. Implement strStr()

Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Examples
Example 1:
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

Example 2:
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's `strstr()` and Java's `indexOf()`.


### Benchmarks and Remarks

```
 Runtime: 32 ms, faster than 91.13% of Python3 online submissions for Implement strStr().
 Memory Usage: 13.9 MB, less than 7.46% of Python3 online submissions for Implement strStr().
 Runtime: 32 ms, faster than 91.13% of Python3 online submissions for Implement strStr().
 Memory Usage: 14.1 MB, less than 7.09% of Python3 online submissions for Implement strStr().
```

Python has some built-ins to make it an easy one-liner.

We do one pass from the start of the haystack, until the point where our needle doesn't fit anymore.

At each of these points, there's a string comparison, to see if we've found the first occurence of our needle. Generally, string comparisons do a linear scan of the character and return false at the first index where the characters do not match. Worst-case time complexity is for each search O(m), and the actual time depends on how many characters need to be scanned before a difference is encountered. After seeing that the characters don't match, we can "leapfrog" the unmatched characters.


There are many string-finding, advanced algorithm, but at the simplest case, if N is the input string, and m is the length of the needle, we have N-m passes. Each pass will take at least 1 comparison, and at most m comparisons. In these cases, it will move either 1 step ahead or m-1 steps ahead. So on average, the whole naive approach might take (N-m)(m/2) ≈ Nm - m².

More advanced algorithms such as KMP might take O(m+N) time, or Booyer-Moore that might take between O(m/N) and O(mN)

