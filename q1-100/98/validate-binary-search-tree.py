## Recursion

# Runtime: 48 ms, faster than 91.76% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 17.1 MB, less than 5.23% of Python3 online submissions for Validate Binary Search Tree.
# Runtime: 52 ms, faster than 74.47% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.9 MB, less than 5.23% of Python3 online submissions for Validate Binary Search Tree.
# Runtime: 48 ms, faster than 91.76% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.9 MB, less than 5.23% of Python3 online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def recurse(node: TreeNode, left: float, right: float) -> bool:
            
            if not node:
                return True
            
            val = node.val
            
            if not recurse(node.right, val, right):
                return False
            
            if not recurse(node.left, left, val):
                return False
            
            if val <= left or val >= right :
                return False
            
            return True
        
        # Would return error for too large values. 
        # There's no standard designed for an integer infinity, 
        # IEEE FP does though
        return recurse(root, float('-inf'), float('+inf'))



## Iterative DFS

# Runtime: 48 ms, faster than 91.76% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16 MB, less than 29.37% of Python3 online submissions for Validate Binary Search Tree.
# Runtime: 52 ms, faster than 74.47% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.1 MB, less than 25.66% of Python3 online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root :
            return True
        
        stack = [
            (root, float('-inf'), float('+inf')),
        ]
        while stack:
            node, left, right = stack.pop()
            if not node:
                continue
            val = node.val
            if val <= left or val >= right:
                return False
            
            stack.append((node.right, val, right))
            stack.append((node.left, left, val))
        return True
            


# DFS Inorder

# Runtime: 52 ms, faster than 74.47% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.2 MB, less than 21.77% of Python3 online submissions for Validate Binary Search Tree.
# Runtime: 52 ms, faster than 74.47% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.3 MB, less than 18.15% of Python3 online submissions for Validate Binary Search Tree.
# Runtime: 48 ms, faster than 91.76% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.3 MB, less than 15.78% of Python3 online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        
        return True


## Another Inorder Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre != None and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True


## General Inorder Traversal using a stack
def inorder_traversal(root: TreeNode):
    lst, stack = [], []
    if root == None :
        return lst

    while root != None or len(stack) != 0:
        while root != None:
            stack.append(root)
            root = root.left
        root = stack.pop
        lst.append(root.val)
        root = root.right
        
return lst
    

