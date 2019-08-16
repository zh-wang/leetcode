"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        cp = {}
        q = []
        q.append(node)
        if node not in cp:
            new_node = Node(node.val, [])
            cp[node] = new_node
        while q:
            cur_node = q.pop()
            for k in cur_node.neighbors:
                if k not in cp: # k is not visited
                    new_k = Node(k.val, [])
                    cp[k] = new_k
                    q.append(k) # add k to queue
                cp[cur_node].neighbors += [cp[k]]
        return cp[node]
