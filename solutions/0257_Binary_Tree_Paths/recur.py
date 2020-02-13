# --Link--
# https://www.lintcode.com/problem/binary-tree-paths/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        self.ret = []
        self.recur(root, [])
        return self.ret

    def recur(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path += [node.val]
            self.ret += [('->'.join(map(str, path)))]
            return
        self.recur(node.left, path + [node.val])
        self.recur(node.right, path + [node.val])
