class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        dset = DisjointSet([i for i in range(n)])
        visited = [False] * n
        for e in edges:
            visited[e[0]] = True
            visited[e[1]] = True
            if dset.find(e[0]) == dset.find(e[1]):
                return False
            else:
                dset.union(e[0], e[1])
        # check all node in DisjointSet share a same parent node
        p = -1
        for v in range(n):
            if p < 0:
                p = dset.find(v)
                continue
            if p != dset.find(v):
                return False
        return True

class DisjointSet:
    def __init__(self, data):
        # an array stores the original data
        self.data = data[:]

        # an array stores index of its parent
        # during init, set parent[i] = i
        # if parent[i] == i, then i represents a set root
        # other index can its representation by `find` method
        self.parents = [i for i in range(len(data))]

        # an array stores rank(height of tree) for const time union
        self.rank = [0] * len(data)

    def union(self, a, b):
        arep = self.find(a) # a's representation
        brep = self.find(b) # b's representation
        if arep == brep: # no need to merge if a and b are in same set
            return
        if self.rank[arep] < self.rank[brep]:
            self.parents[arep] = brep
        elif self.rank[arep] > self.rank[brep]:
            self.parents[brep] = arep
        else:
            self.parents[arep] = brep
            self.rank[brep] += 1

    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            represent = self.find(self.parents[i])
            # path compression
            # link node to its representation
            self.parents[i] = represent
            return represent

