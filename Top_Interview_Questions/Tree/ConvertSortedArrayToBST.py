# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        if len(nums) != 1:
            root.left = self.sortedArrayToBST(nums[:mid])
            if (len(nums)-1) != mid:
                root.right = self.sortedArrayToBST(nums[mid+1:])
        return root