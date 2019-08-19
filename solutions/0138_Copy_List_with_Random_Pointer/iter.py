"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cp = {}
        runner = head
        while runner:
            cp_node = self.getOrNew(runner, cp)
            cp_node.next = self.getOrNew(runner.next, cp)
            cp_node.random = self.getOrNew(runner.random, cp)
            runner = runner.next
        return cp[head]

    def getOrNew(self, node, cp):
        if not node:
            return None
        if node not in cp:
            cp[node] = Node(node.val, None, None)
        return cp[node]
