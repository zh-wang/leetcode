class Solution:
    def numberOfConnectedComponents(self, n, edges):
        dset = DisjointSet([i for i in range(n)])
        for e in edges:
            pa, pb = dset.find(e[0]), dset.find(e[1])
            if pa != pb:
                dset.union(e[0], e[1])
        reps = [dset.find(i) for i in range(n)]
        return len(set(reps))

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
