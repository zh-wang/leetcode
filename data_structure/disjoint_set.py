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

        self.weight = [1] * len(data)
        self.maxWeight = 0

        # hashmap to find index of value
        self.dic = defaultdict(lambda: -1)
        for i in range(len(data)):
            self.dic[data[i]] = i

    def union(self, a, b):
        arep = self.find(a) # a's representation
        brep = self.find(b) # b's representation
        if arep == brep: # no need to merge if a and b are in same set
            return
        if self.rank[arep] < self.rank[brep]:
            self.parents[arep] = brep
            self.weight[brep] += self.weight[arep]
            self.maxWeight = max(self.maxWeight, self.weight[brep])
        elif self.rank[arep] > self.rank[brep]:
            self.parents[brep] = arep
            self.weight[arep] += self.weight[brep]
            self.maxWeight = max(self.maxWeight, self.weight[arep])
        else:
            self.parents[arep] = brep
            self.weight[brep] += self.weight[arep]
            self.maxWeight = max(self.maxWeight, self.weight[brep])
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

    def selfmerge(self):
        for i in range(len(self.data)): # for each set
            a = self.dic[self.data[i]]
            b = self.dic[self.data[i] - 1]
            if b >= 0:
                self.union(a, b)
            c = self.dic[self.data[i] + 1]
            idf c >= 0:
                self.union(a, c)

    def debug(self):
        for i in range(len(self.parents)):
            print(self.parents[i])

data = [rd.randrange(100) for i in range(30)]
dset = DisjointSet(data)
dset.debug()
print("========")
print(data)
dset.selfmerge()
dset.debug()
