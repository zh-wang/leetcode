# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.ret = TreeNode(0) # dummy node, return its right child
        self.head = self.ret
        self.recur(root, [])
        return self.ret.right

    # store right child on a stack
    # recur first on left child
    # if no left child exists, pop from the stack
    def recur(self, root, stack):
        if not root:
            if stack: # if stack has elements, pop one then recur on it
                self.recur(stack.pop(), stack)
            return
        self.head.right = root # set current node to head's right child
        stack.append(root.right) # push right child to stack
        root.right = None # remove connection to right child
        left = root.left # keep left child
        root.left = None # remove connection to left child
        self.head = root # move head forward
        self.recur(left, stack)
