
class Solution:

    def numIslands(self, m, n, positions):
        imap = [[-1 for _ in range(n)] for _ in range(m)]
        dset = DisjointSet([i for i in range(len(positions))])
        curSetIndex = 0
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for p in positions:
            imap[p[0]][p[1]] = curSetIndex
            for dir in dirs:
                x, y = p[0] + dir[0], p[1] + dir[1]
                if 0 <= x < m and 0 <= y < n and imap[x][y] >= 0:
                    dset.union(imap[x][y], curSetIndex)
            curSetIndex += 1
        return dset.numOfSets()

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

    def numOfSets(self):
        ret = 0
        for i in range(len(self.parents)):
            if i == self.parents[i]:
                ret += 1
        return ret

    def debug(self):
        for i in range(len(self.parents)):
            print(i, self.parents[i])

positions = [
        [0, 0],
        [2, 0],
        [1, 0],
        [1, 1],
        [3, 3],
        [4, 4],
        [4, 0],
        [3, 4],
        [4, 3]
        ]
x = Solution().numIslands(5, 5, positions)
print(x)
