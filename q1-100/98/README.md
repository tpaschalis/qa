# 98. Validate Binary Search Tree

Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

### Examples
```
Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
```
```
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```


### Testcases
```
[2,1,3]
[5,1,4,null,null,3,6]
[2147483647]
```

### Benchmarks and Remarks

Fastest I got was
```
 Runtime: 48 ms, faster than 91.76% of Python3 online submissions for Validate Binary Search Tree.
 Memory Usage: 17.1 MB, less than 5.23% of Python3 online submissions for Validate Binary Search Tree.
```
A couple of different ways around the problem. A recursive solution, checking at each node, an iterative Depth-First Search using a stack, and a in-order node traversal (each node will have to be lower than the next one).
