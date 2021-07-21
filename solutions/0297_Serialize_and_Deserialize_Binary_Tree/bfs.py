# STAR

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        q = deque()
        q.append(root)
        ret = []
        while q:
            cur = q.popleft()
            if cur == None:
                ret += ['#']
                continue
            ret += [cur.val]
            q.append(cur.left)
            q.append(cur.right)
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        q = deque()
        root = TreeNode(data[0])
        q.append(root)
        n = len(data)
        i = 0
        while q:
            node = q.popleft()
            li = i + 1
            if li < n and data[li] != '#':
                node.left = TreeNode(data[li])
                q.append(node.left)
            ri = i + 2
            if ri < n and data[ri] != '#':
                node.right = TreeNode(data[ri])
                q.append(node.right)
            i = ri
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
