# 195. Tenth Line

Easy

Given a text file file.txt, print just the 10th line of the file.

### Examples

Assume that file.txt has the following content:
```
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```

Your script should output the tenth line, which is:
```
Line 10
```

Note:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.


### Benchmarks and Remarks

```
 Runtime: 0 ms, faster than 100.00% of Bash online submissions for Tenth Line.
 Memory Usage: 3.7 MB, less than 45.63% of Bash online submissions for Tenth Line.
```
Sed ftw. head/tail can be another option, but might be slower for a large file.
