# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        pairs = {}
        st = []
        for i, c in enumerate(s):
            if c == '[':
                st += [i]
            elif c == ']':
                pairs[st.pop()] = i

        def recur(s, l, r, is_list=True):
            ret = NestedInteger()
            i = l
            temp = ''
            while i <= r:
                if s[i] == '[':
                    ret.add(recur(s, i + 1, pairs[i] - 1))
                    i = pairs[i]
                elif s[i] == ',':
                    if temp:
                        ret.add(NestedInteger(int(temp)))
                        temp = ''
                else:
                    temp += s[i]
                i += 1
            if temp:
                ret.add(NestedInteger(int(temp))) if is_list else ret.setInteger(int(temp))
            return ret

        if s[0] == '[':
            return recur(s, 1, len(s) - 2, is_list=True)
        else:
            return recur(s, 0, len(s) - 1, is_list=False)

