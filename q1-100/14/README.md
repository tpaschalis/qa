# 14. Longest Common Prefix

Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Note:

All given inputs are in lowercase letters a-z.

### Examples

Example 1:
```
Input: ["flower","flow","flight"]
Output: "fl"
```

Example 2:
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Testcases
```
["flower","flow","flight"]
["aa","a"]
["c","c"]
[""]
```

### Benchmarks and Remarks

```
 Runtime: 28 ms, faster than 99.11% of Python3 online submissions for Longest Common Prefix.
 Memory Usage: 13.3 MB, less than 31.04% of Python3 online submissions for Longest Common Prefix.
```

I have implemented five basic approaches; horizontal scanning, vertical search, using Python's built-in zip lists and sets, a recursive Divide and Conquer, and a Binary Search.

Binary Search was the fastest of them all.

- Horizontal Scanning : O(S) in time, where "S" is the sum of all characters, in all strings. In the worst case, all n strings are the same, and the algorithm would compare all of them with each another. Space complexity is O(1)

- Vertical Scanning : Again, O(S) in time. In the worst case though, there will be n equal string with length m, and the algorithm will still perform S = m × n comparisons. The difference is in the best case, where there are *at most* n × minimumLengthString. Space complexity is O(1)

- For Divide and Conquer, if S is the number of all characters in the input array, S = m×n, Time Complexity would be 2×T(n/2) + O(m) = O(S). The best case is O(n×minLen) comparisons. Space complexity is not constant any more, and is O(m×logn), since we store recursive calls in the execution stack. There are logn recursive calls, and each needs to store m-length results.

- For Binary Search, Time Complexity is no longer O(S), but O(S×logn)! The algorithm will take up logn iterations, each of them contains S=m×n comparisons. Space complexity is constant.

