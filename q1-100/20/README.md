# 20. Valid Parentheses

Hard

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.


### Examples

Example 1:
```
Input: "()"
Output: true
```

Example 2:
```
Input: "()[]{}"
Output: true
```

Example 3:
```
Input: "(]"
Output: false
```

Example 4:
```
Input: "([)]"
Output: false
```

Example 5:
```
Input: "{[]}"
Output: true
```


### Testcases
```
()
((()))
(()()())
{()[][()()]}
```

### Benchmarks and Remarks

```
# Part 1
 Runtime: 32 ms, faster than 92.31% of Python3 online submissions for Valid Parentheses.
 Memory Usage: 13.2 MB, less than 72.61% of Python3 online submissions for Valid Parentheses

# Part 2
 Runtime: 32 ms, faster than 92.31% of Python3 online submissions for Valid Parentheses.
 Memory Usage: 13.4 MB, less than 8.99% of Python3 online submissions for Valid Parentheses.
```

Python optimizes the solutions with the same ideas under the hood. Complexity is O(n) for time, as we're just passing through the input once, and O(n) for space, because the stack can be as big as the input itself. For valid solutions, the space will be less than O(n/2).

I'm going to take a look into a recursive solution. It might sacrifice time complexity, but should be constant in space.
