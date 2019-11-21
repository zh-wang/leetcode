class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None

    def startWith(self, prefix):
        node = self.root
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        return True

    def contains(self, word):
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        return True if '$' in node else False

trie = Trie()
trie.insert("asdf")
trie.insert("asfewji")
trie.insert("asfeiwfj")
trie.insert("asss")
trie.insert("asfe")
trie.insert("a")

print(trie.startWith('as'))
print(trie.startWith('asfefw'))
print(trie.contains('asfeiwfj'))
print(trie.contains('asfeiwfx'))

# def dfs(node, d):
    # if node.isEnd:
        # return
    # for i, next in enumerate(node.links):
        # if next is not None:
            # print(chr(i + 97), d)
            # dfs(next, d + 1)

# dfs(trie.root, 0)

# def lps(node, d):
    # if node.isEnd:
        # return d
    # cnt = 0
    # next = None
    # for node in node.links:
        # if node is not None:
            # cnt += 1
            # next = node
    # if cnt == 1:
        # return lps(next, d + 1)
    # return d

# dfs(trie.root, 0)
# print(lps(trie.root, 0))
