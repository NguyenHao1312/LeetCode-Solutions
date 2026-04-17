class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total