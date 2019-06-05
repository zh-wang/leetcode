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
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if not node.containsKey(c):
                node.put(c, TrieNode())
            node = node.get(c)
        node.setEnd()

trie = Trie()
trie.insert("asdf")
trie.insert("asfewji")
trie.insert("asfeiwfj")
trie.insert("asss")
trie.insert("asfe")
trie.insert("a")

def dfs(node, d):
    if node.isEnd:
        return
    for i, next in enumerate(node.links):
        if next is not None:
            print(chr(i + 97), d)
            dfs(next, d + 1)

# dfs(trie.root, 0)

def lps(node, d):
    if node.isEnd:
        return d
    cnt = 0
    next = None
    for node in node.links:
        if node is not None:
            cnt += 1
            next = node
    if cnt == 1:
        return lps(next, d + 1)
    return d

print(lps(trie.root, 0))
