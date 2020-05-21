# 6. ZigZag Conversion

Medium


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```


### Examples

Example 1:
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

### Testcases
```
"ABC"
1

"ABCD"
3

"PAS"
6

"PAYPALISHIRINGGOFAST"
5
```

### Benchmarks and Remarks

```
 Runtime: 48 ms, faster than 99.73% of Python3 online submissions for ZigZag Conversion.
 Memory Usage: 13.2 MB, less than 74.70% of Python3 online submissions for ZigZag Conversion.
```

I tried **two different approaches**: 

1. The first approach was to go row by row, and calculate all the indices we need for each row.    
An example, if `M = numRows - 2`.

```
0	   M                       2M
1     M-1      M+1           2M-1     2M+1
2  M-2           M+2     2M-2            2M+2
.
.
.

```

On my first approach, I was calculating `0, M, 2M..` for the first row, `1, M-1, M+1, 2M-1, 2M+1` for the second row, etcetera etcetera.

It was cumbersome, because the top and bottom row require are edge cases, and we always need to check that our `nM +- i` index is valid. When I started thinking if I should use a ternary operator, it was time to move on to something else.

2. The second approach is *so much cleaner and easier*.

Rather than going through each row, we go character by character, and assign them to each row. Starting from char 0, we need to assign each subsequent character to the next row. When we reach numRows, we need to reverse the sign, and assign subsequent characters to previous rows, and keep doing that ping-pong between 0 and numRows, until we run out of characters.

```
0							0
1						1		1
2					2				2
..				..						..
..			numRows - 2							numRows - 2
numRows -1 	numRows - 1								 	numRows - 1
numRows													numRows

```

So we just need to keep track of 
- the current letter
- the 'row' we're assigning it
- if the next letter is going to be assign to the previous or the next row (our step).

The complexity is O(n)


