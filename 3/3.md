# 3. Longest Substring Without Repeating Characters

Medium

Given a string, find the length of the longest substring without repeating characters.


### Examples 

Example 1:
```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

Example 2:
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```


### Testcases
```
"abcabcbb"
"bbbbbbbb"
"pwwkey"
"aaaaaaaaaaaaaaaanaaanaamaldpqddddddddddddddd"
"a"
```

### Benchmarks and Remarks

```
 Runtime: 36 ms, faster than 89.82% of Python3 online submissions for Two Sum.
 Memory Usage: 14.4 MB, less than 36.74% of Python3 online submissions for Two Sum.
```

 Three basic approaches
 1. Brute-force the entire thing - O(n^3) in time, O(min(n,m)) space, depending on the size of the string n and the size of the possible characters m
 2. Use a sliding window, and a hash map for constant-time lookups. Use the window between [i-j), search for matches, and slide the window. If a match is found, start from the next i. This is O(2*n) in time, and again, O(min(n,m)) in space.
 3. We can do it in one pass as well. The hash map can hold the mapping of a character to its index, so we skip all duplicate characters in the window. If, in the window `[i, j)`, there's a duplicate in `j'` position, then `i` can 'jump' to `j'+1` immediately.


