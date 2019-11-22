class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        nodes = [self.root] # a list of nodes we want to search. At the beginning, only root
        for c in word:
            new_nodes = []
            if c == '.':
                new_nodes += [ node[entry] for node in nodes for entry in node ]
            else:
                new_nodes += [ node[entry] for node in nodes for entry in node if entry == c ]
            nodes = new_nodes
        return '$' in [ entry for node in nodes for entry in node ]



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
