# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            childNodes = [root.left, root.right]
            while True:
                if all(childNode == None for childNode in childNodes):
                    return True
                if self.isLayerSymmetric(childNodes):
                    tmp = []
                    for childNode in childNodes:
                        if childNode == None:
                            tmp.append(None)
                            tmp.append(None)
                        else:
                            tmp.append(childNode.left)
                            tmp.append(childNode.right)
                    childNodes = tmp
                    continue
                return False
        return True
    def isLayerSymmetric(self, childNodes) -> bool:
        for i in range(int(len(childNodes)/2)):
            if childNodes[i] and childNodes[len(childNodes)-1-i]:
                if childNodes[i].val != childNodes[len(childNodes)-1-i].val:
                    return False
            if not childNodes[i] and not childNodes[len(childNodes)-1-i]:
                continue
            if not childNodes[i] or not childNodes[len(childNodes)-1-i]:
                return False
        return True