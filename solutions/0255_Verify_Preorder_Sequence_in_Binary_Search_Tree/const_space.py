# --STAR-- --Link--
# https://www.lintcode.com/problem/verify-preorder-sequence-in-binary-search-tree/description

class Solution:
    """
    @param preorder: List[int]
    @return: return a boolean
    """
    def verifyPreorder(self, preorder):
        # write your code here
        low = -1 << 32
        index = -1 # use preorder as a stack, this is the stack's top
        for v in preorder:
            if v < low:
                return False
            while index >= 0 and preorder[index] < preorder[i]:
                low = preorder[index]
                index -= 1
            preorder[index] = preorder[i]
            index += 1
        return True
