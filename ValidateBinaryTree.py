# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        maxval = math.inf
        minval= -math.inf
        
        def check(node, minval, maxval):
            if not minval < node.val < maxval:
                return False
            if node.right:
                right=check(node.right, node.val, maxval) 
            else: 
                right=True
            if node.left:
                left= check(node.left, minval, node.val)
            else: 
                left=True
            return left and right
        return check (root, minval, maxval)
