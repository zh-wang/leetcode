class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = [root]
        while q:
            runner = Node() # dummy head, no use later
            next_q = []
            for node in q:
                runner.next = node
                runner = runner.next
                if node.left:
                    next_q += [node.left]
                if node.right:
                    next_q += [node.right]
            q = next_q[:]
        return root
