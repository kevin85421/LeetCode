# Tree
## Overview
*   **Easy:** Q1 ~ Q5
*   **Medium:**
*   **Worth it:** Q1, Q2
## Q1: Maximum Depth of Binary Tree
### My Solution
*   Recursive (DFS)
*   TODO: try BFS
*   Clean version
```python
def maxDepth(self, root: TreeNode) -> int:
    if root == None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
## Q2: Valid Binary Search Tree
### My Solution
*   In-order traversal (Recursive) 
*   Check if the list is sorted
*   Time Complexity: `O(n)` --> Complexity is OK, but it can be more efficient
*   Space Complexity: `O(n)`
### LeetCode Solution: [Link](https://leetcode.com/problems/validate-binary-search-tree/solution/)
*   Approach 1: Recursion Approach
    *   upper/lower (start from root)
    *   Time Complexity: `O(n)`
    *   Space Complexity: `O(n)`
```python
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
```
*   Approach 2: Iteration
    *   upper/lower (start from root)
    * Time Complexity: `O(n)`
    * Space Complexity: `O(n)`
```python
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True  
```
*   Approach 3: Inorder traversal
    * lower bound only (start from the leftmost node)
    * Time Complexity: `O(n)`
    * Space Complexity: `O(n)`
```python
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
```