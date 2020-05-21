# 38. Count and Say

Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:

```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

### Examples

Example 1:
```
Input: 1
Output: "1"
```

Example 2:
```
Input: 4
Output: "1211"
```

### Testcases
```
1
3
10
```

### Benchmarks and Remarks

```
 Runtime: 20 ms, faster than 77.80% of Python online submissions for Count and Say.
 Memory Usage: 11.7 MB, less than 92.37% of Python online submissions for Count and Say.
```

We can use itertools, regular expressions, or build the function reading the numbers out loud ourselves. Solution is O(nm)

