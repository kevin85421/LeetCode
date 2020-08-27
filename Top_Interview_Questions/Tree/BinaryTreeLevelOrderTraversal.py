# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        layer = []
        q = [root]
        while q:
            parentNode = q.pop(0)
            if parentNode.left:
                layer.append(parentNode.left)
            if parentNode.right:
                layer.append(parentNode.right)
            if not q:
                tmp = []
                for node in layer:
                    q.append(node)
                    tmp.append(node.val)
                if tmp:
                    res.append(tmp)
                layer = []
        return res