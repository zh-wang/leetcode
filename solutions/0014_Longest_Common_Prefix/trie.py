class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        trie = Solution.Trie()
        for s in strs:
            trie.insert(s)
        return strs[0][:self.lps(trie.root, 0)]

    def lps(self, node, d):
        if node.isEnd:
            return d
        cnt = 0
        next = None
        for node in node.links:
            if node is not None:
                cnt += 1
                next = node
        if cnt == 1:
            return self.lps(next, d + 1)
        return d

    class TrieNode(object): # work for 'a'-'z'
        def __init__(self):
            self.R = 26
            self.links = [None] * self.R
            self.isEnd = False

        def containsKey(self, s):
            return self.links[ord(s) - 97] is not None

        def get(self, s):
            return self.links[ord(s) - 97]

        def put(self, s, node):
            self.links[ord(s) - 97] = node

        def setEnd(self):
            self.isEnd = True

    class Trie(object):
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert(self, word):
            node = self.root
            for c in word:
                if not node.containsKey(c):
                    node.put(c, Solution.TrieNode())
                node = node.get(c)
            node.setEnd()
