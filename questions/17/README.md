# 17. Letter Combinations of a Phone Number

Medium

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the old-school telephone buttons) is given below. Note that 1 does not map to any letters.


### Examples

Example:
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

### Testcases
```
""
"23"
"2662"
```

### Benchmarks and Remarks

```
 Runtime: 28 ms, faster than 98.57% of Python3 online submissions for Letter Combinations of a Phone Number.
 Memory Usage: 13.2 MB, less than 40.39% of Python3 online submissions for Letter Combinations of a Phone Number.
```

Again, same base ideas with slightly different expressions yield same-ish times.

I'm just looping through previous set at each iteration, and then appending the values of the dictionary key that matches my current digit.

Time and Space complexity are O(3^n × 4^m), where n, m the number of digits that map to 3-letter buttons and 4-letter buttons correspondingly. n+m equals to the total number of input digits.
