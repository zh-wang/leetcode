# --STAR-- --Link--
# https://www.lintcode.com/problem/verify-preorder-sequence-in-binary-search-tree/description

class Solution:
    """
    @param preorder: List[int]
    @return: return a boolean
    """
    def verifyPreorder(self, preorder):
        # write your code here
        return self.verify(preorder, 0, len(preorder))

    def verify(self, arr, s, t):
        if s + 1 >= t:
            return True
        pivot = arr[s]
        i, j = s + 1, 0
        while i < t and arr[i] < pivot:
            i += 1
        j = i
        while i < t and arr[i] > pivot:
            i += 1
        if i < t:
            return False
        return self.verify(arr, s + 1, j) and self.verify(arr, j + 1, t)
