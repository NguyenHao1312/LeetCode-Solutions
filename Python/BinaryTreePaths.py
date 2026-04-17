class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def BinaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        for path in self.BinaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)
        for path in self.BinaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)
        return paths