class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        # In a binary tree, if we consider null as leaves, then
        # all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
        # Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree. When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by2, because it provides two out degrees. If a serialization is correct, diff should never be negative and diff will be zero when finished.
        diff = 1
        for v in arr:
            # each node provide a indgree
            diff -= 1
            if diff < 0: # indgree larger than outdgree
                return False
            if v != '#':
                diff += 2 # non-empty node provide two outdgrees
        return diff == 0 # indgree must be equal to outdgree
