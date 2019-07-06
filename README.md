# leetcode-answers

| # | Title | Solution | Difficulty | Basic idea (One line) |
|---| ----- | -------- | ---------- | --------------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python]() | Easy | One-pass hash table solution is available. O(n) in time and space. Bruteforce is  O(n²)/O(1) |
| 3 | [Longest Substring w/o Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [Python]() | Medium | Avoid bruteforce w/ a Sliding Window and a Hash map. Optimize by skipping repeated chars |
| 4 | [Median of Two Sorted Arrays - WIP](https://leetcode.com/problems/median-of-two-sorted-arrays) | [Python]() | Hard | Avoid merging the arrays to go from O(m+n) to [O(log(min(m, n)))](https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46). Python optimizations make the naive solution *not terrible*. |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer) | [Python]() | Easy | Either work with string representation or bit manipulation. Check for overflow *after* flipping. O(logx), about log(x) digits in decimal representation of x |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python]() | Easy | Either one-pass with some clever lookahead in O(n), or check for hardcoded exceptions after the pass where O(dependsonyourcompiler). |
|  xx  | [Title]()   | [Language]()  | Difficulty  | Explanation |
