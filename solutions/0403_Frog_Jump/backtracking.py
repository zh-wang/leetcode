class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.distToIndex = {}
        for i, v in enumerate(stones):
            self.distToIndex[v] = i
        k = len(stones)
        # -1 => init, 0 => cannot reach, 1 => can reach
        self.dp = [[-1 for _ in range(k)] for _ in range(k)]
        # first jump is from 0 with 1 unit distance
        self.dp[0][1] = 1

        for d in range(1, len(stones)):
            if self.recur(stones, len(stones) - 1, d) > 0:
                return True
        return False

    # whether frog can jump d units from i-th stone
    def recur(self, stones, i, d):
        if self.dp[i][d] >= 0:
            return self.dp[i][d]

        # the max jump unit from index i will be i + 1
        # because for each jump, we can only inc jump distance by 1 unit
        if d > i + 1:
            self.dp[i][d] = 0
            return 0

        # if frog can jump d - 1, d or d + 1 units from last stone
        # then it can jump d units from here
        if stones[i] - (d + 1) in self.distToIndex and d + 1 < len(stones) \
            and self.recur(stones, self.distToIndex[stones[i] - (d + 1)], d + 1):
            self.dp[i][d] = 1
            return 1
        if stones[i] - (d + 0) in self.distToIndex \
            and self.recur(stones, self.distToIndex[stones[i] - (d + 0)], d + 0):
            self.dp[i][d] = 1
            return 1
        if stones[i] - (d - 1) in self.distToIndex and d - 1 > 0 \
            and self.recur(stones, self.distToIndex[stones[i] - (d - 1)], d - 1):
            self.dp[i][d] = 1
            return 1
        self.dp[i][d] = 0
        return 0
