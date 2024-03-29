# --STAR-- --Link--
# https://www.lintcode.com/problem/verify-preorder-sequence-in-binary-search-tree/description

class Solution:
    """
    @param preorder: List[int]
    @return: return a boolean
    """
    def verifyPreorder(self, preorder):
        # write your code here
        stack = []
        low = -1 << 32
        for v in preorder:
            if v < low:
                return False
            while stack and stack[-1] < preorder[i]:
                stack.pop()
            stack += [v]
        return True
