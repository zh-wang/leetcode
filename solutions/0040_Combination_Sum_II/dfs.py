class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cand = sorted(candidates)
        self.retList = []
        self.recur(cand, 0, target, [])
        return self.retList

    def recur(self, cand, d, target, l):
        if target == 0:
            self.retList.append(l)
        if d >= len(cand) or cand[d] > target:
            return
        # handle duplicates
        s = d
        while d + 1 < len(cand) and cand[d] == cand[d + 1]: # count number of dups
            d += 1
        for i in range(d - s + 2): # pick dups at most (d - s + 1) times
            self.recur(cand, d + 1, target - cand[s] * i, l + [cand[d]] * i)
