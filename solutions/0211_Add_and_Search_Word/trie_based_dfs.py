class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if not node.contains(c):
                node.put(c, TrieNode())
            node = node.get(c)
        node.isEnd = True
        print('{} is added'.format(word))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        print('searching {}'.format(word))
        stack = []
        stack += [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i >= len(word):
                if node.isEnd:
                    return True
                continue
            if word[i] == '.':
                for c in self.chars:
                    if node.contains(c):
                        stack += [(node.get(c), i + 1)]
            else:
                if node.contains(word[i]):
                    stack += [(node.get(word[i]), i + 1)]
        return False

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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
