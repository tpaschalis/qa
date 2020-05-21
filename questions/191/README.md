# 191. Number of 1 Bits

Easy

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).


### Examples

Example 1:

```
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

Example 2:
```
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```

Example 3:
```
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

### Benchmarks and Remarks

```
 Runtime: 0 ms, faster than 100.00% of Go online submissions for Number of 1 Bits.
 Memory Usage: 2 MB, less than 100.00% of Go online submissions for Number of 1 Bits.
```

Basically just dividing by two (eating bits off the number's tail), and keeping track how many of them were ones
