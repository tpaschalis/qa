# 194. Transpose File

Medium

Given a text file file.txt, transpose its content.

You may assume that each row has the same number of columns and each field is separated by the ' ' character.

### Examples

If file.txt has the following content:
```
name age
alice 21
ryan 30
```
Output the following:
```
name alice ryan
age 21 30
```

### Benchmarks and Remarks

```
 Runtime: 8 ms, faster than 85.81% of Bash online submissions for Transpose File.
 Memory Usage: 3.5 MB, less than 89.47% of Bash online submissions for Transpose File.
```

Bash one-liner. Initially I had a `; echo ""` to separate lines, but this came back with silly edge case when having a single column as input.

`xargs` works fine as well

