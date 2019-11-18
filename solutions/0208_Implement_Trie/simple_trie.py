class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if not node.contains(c):
                node.put(c, TrieNode())
            node = node.get(c)
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if not node.contains(c):
                return False
            node = node.get(c)
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if not node.contains(c):
                return False
            node = node.get(c)
        return True

class TrieNode:

    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False

    def contains(self, c):
        return self.links[ord(c) - 97] is not None

    def get(self, c):
        return self.links[ord(c) - 97]

    def put(self, c, node):
        self.links[ord(c) - 97] = node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
