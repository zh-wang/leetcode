# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [] # stack stores tuple: (TreeNode, Its_Left_Child_Is_Visited)
        # (Node, False) => Node's left child is not visited
        # (Node, True) => Node's right child is not visited
        # If both children are visited, Node will be removed from stack
        if root: # handle special case: root is None
            self.stack.append((root, False))

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.stack:
            return -1
        while self.stack:
            node, l_visited = self.stack.pop()
            if node.left and not l_visited:
                self.stack.append((node, True))
                self.stack.append((node.left, False))
            else:
                ret = node.val
                if node.right:
                    self.stack.append((node.right, False))
                return ret
        return -1

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.stack:
            return False
        if self.stack[-1][0].left: # if last running node has left child, we can ensure that next element exists
            return True
        i = len(self.stack) - 1 # otherwise, we climb up along stack to find a node whose right child is not visited
        while i >= 0 and self.stack[i][1]:
            i -= 1
        return i >= 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

        # if not root:
            # return []
        # ret = []
        # stack = []
        # stack.append((root, False))
        # while stack:
            # node, l_visited = stack.pop()
            # if node.left and not l_visited:
                # stack.append((node, True))
                # stack.append((node.left, False))
            # else:
                # ret.append(node.val)
                # if node.right:
                    # stack.append((node.right, False))
        # return ret
