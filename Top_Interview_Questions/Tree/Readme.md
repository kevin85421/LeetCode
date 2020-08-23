# Tree
## Overview
*   **Easy:** Q1
*   **Medium:**
*   **Worth it:** Q1
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