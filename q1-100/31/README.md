# 31. Next Permutation

Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

### Examples
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
```

### Testcases
```
[1,2,3]
[1,3,2]
[1,5,8,4,7,6,5,3,1]
```

### Benchmarks and Remarks

```
 Runtime: 44 ms, faster than 60.41% of Python3 online submissions for Next Permutation.
 Memory Usage: 13.9 MB, less than 5.20% of Python3 online submissions for Next Permutation.
```

Nice trick required for [lexicographic order](https://stackoverflow.com/questions/1622532/algorithm-to-find-next-greater-permutation-of-a-given-string?answertab=active#tab-top) generation. O(n) time algorithm since at most two traversals are needed. As per the requirement space is constant.
