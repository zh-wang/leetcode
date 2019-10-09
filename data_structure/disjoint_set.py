class DisjointSet:
    def __init__(self, data):
        # an array stores index of its parent
        # during init, set parent[i] = i
        self.parents = [i for i in range(len(data))]

    def union(self, set_a, set_b):
        pass

    def find(self, node):
        pass
