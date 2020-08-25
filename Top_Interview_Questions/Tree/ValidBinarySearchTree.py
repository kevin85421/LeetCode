# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        in_order = self.inorderTraversal(root)
        if all(in_order[i] < in_order[i+1] for i in range(len(in_order)-1)):
            return True
        return False
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left) 
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res