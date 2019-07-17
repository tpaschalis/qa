# 22. Generate Parentheses

Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Examples

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```


### Testcases

```
1
3
5
```

### Benchmarks and Remarks

```
 Runtime: 28 ms, faster than 99.91% of Python3 online submissions for Generate Parentheses.
 Memory Usage: 13.5 MB, less than 25.30% of Python3 online submissions for Generate Parentheses.

 Runtime: 36 ms, faster than 94.01% of Python3 online submissions for Generate Parentheses.
 Memory Usage: 13.5 MB, less than 29.84% of Python3 online submissions for Generate Parentheses.
```

Like in the problem of checking if a parentheses string is valid, we use backtrack. We keep track of each set we create, and if we can add more left or right parentheses.

This recursive solution's complexity is not easy to come up with on the spot, but is the n-th Catalan number, at both time and space : O(Cat(n)), bounded by O(4ⁿ/√n)
