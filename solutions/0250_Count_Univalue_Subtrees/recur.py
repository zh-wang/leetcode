# --STAR-- --Link--
# https://www.lintcode.com/problem/count-univalue-subtrees/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtrees(self, root):
        # write your code here
        return self.cal(root)[1]

    """
    @return: (isValidSubtree, # of subtrees)
    """
    def cal(self, root):
        if not root: # leaf is always valid, but count as 0 subtrees
            return (True, 0)
        l = self.cal(root.left)
        r = self.cal(root.right)
        if not l[0] or not r[0]: # root has invalid child
            return (False, l[1] + r[1])
        # both children are valid
        leq = not root.left or root.left.val == root.val
        req = not root.right or root.right.val == root.val
        if leq and req:
            return (True, l[1] + r[1] + 1)
        return (False, l[1] + r[1])
