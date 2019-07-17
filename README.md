# leetcode-answers

| # | Title | Solution | Difficulty | Basic idea (One line) |
|---| ----- | -------- | ---------- | --------------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/1) | Easy | One-pass hash table solution is available. O(n) in time and space. Bruteforce is  O(n²)/O(1) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/2)  | Medium  | O(max(m, n)) in both time and space. Remember to loop once again if the carry is not zero. |
| 3 | [Longest Substring w/o Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/3) | Medium | Avoid bruteforce w/ a Sliding Window and a Hash map. Optimize by skipping repeated chars |
| 4 | [Median of Two Sorted Arrays - WIP](https://leetcode.com/problems/median-of-two-sorted-arrays) | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/4) | Hard | Avoid merging the arrays to go from O(m+n) to [O(log(min(m, n)))](https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46). Python3 optimizations make the naive solution *not terrible*. |
| 6  | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/xx)  | Medium  | Single-pass O(n) solution. Rather than going through each 'row', work char-by-char |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer) | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/7) | Easy | Either work with string representation or bit manipulation. Check for overflow *after* flipping. O(logx), about log(x) digits in decimal representation of x |
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/8)  | Medium  | Single-pass silly problem. Python3 optimization is fast |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/9)  | Easy  | Constant Space disallows strings. Complexity is O( (logn)/2 ) as we divide as many as (½ input digits) times |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/submissions/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/11)  | Medium  | Single-pass O(n) solution, working with left/right pairs |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/12)  | Medium  |  |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/13) | Easy | Either one-pass with some clever lookahead in O(n), or check for hardcoded exceptions after the pass where O(dependsonyourcompiler). |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/14)  | Easy  | Options : Binary Search, Zip List built-in, Divide and Conquer, and Vertical/Horizontal scanning |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/17)  | Medium | Itertools-like problem, at each step get the state and add possible combinations. O(3^n × 4^m) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/19)  | Medium  | Either two-pass with one pointer and *2L-n* operations or single traversal with two pointers and O(L) complexity |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/20)  | Easy | Not really hard. Either use stack for O(n) time/space, or recursion for constant space and [O(n*Cat(n))](https://en.wikipedia.org/wiki/Catalan_number) time |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)   | [Python3](https://github.com/tpaschalis/qa/tree/dev/q1-100/22)  | Medium  | Using backtracking like in #20. O(4ⁿ/√n), the bound of the n-th Catalan number |
|  xx  | [Title]()   | [Language](https://github.com/tpaschalis/qa/tree/dev/q1-100/xx)  | Difficulty  | Explanation |
