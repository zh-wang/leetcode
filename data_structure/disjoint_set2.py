from collections import defaultdict
import random as rd

class DisjointSet:
    def __init__(self, data):
        # an array stores the original data
        self.data = data[:]

        # an array stores index of its parent
        # during init, set parent[i] = i
        # if parent[i] == i, then i represents a set
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

data = [i for i in range(10)]
dset = DisjointSet(data)
dset.union(2, 3)
dset.union(3, 4)
dset.union(6, 9)
dset.union(4, 9)
print("====")
for i in range(10):
    print(dset.find(i))
