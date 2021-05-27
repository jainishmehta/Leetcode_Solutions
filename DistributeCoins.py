# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        
        def depthfirstsearch(node):
            if not node: return 0
            L,R= depthfirstsearch(node.left), depthfirstsearch(node.right)
            self.ans += abs(L)+abs(R)
            return node.val+L+R-1
        
        depthfirstsearch(root)
        return self.ans
        
