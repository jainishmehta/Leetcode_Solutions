# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
        :type root: TreeNode
        :rtype: List[int]
"""
class Solution(object):
    def inorderTraversal(self, root):
        if not root: return []
        return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)
        
