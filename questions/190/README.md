# 190. Reverse Bits

Easy

Reverse bits of a given 32 bits unsigned integer.

 



### Examples

Example 1:
```
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

Example 2:
```
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

### Benchmarks and Remarks

```
 Runtime: 0 ms, faster than 100.00% of Go online submissions for Reverse Bits.
 Memory Usage: 2.5 MB, less than 25.00% of Go online submissions for Reverse Bits.
```

This is very similar to #191. Just bits off the end of the input, shifting right, and add them to the output, shifting left.

You'll have to do this for the whole 32 bits, so that you don't miss leading (trailing) zeroes out.
