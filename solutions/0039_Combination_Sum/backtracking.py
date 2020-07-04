class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ansList = []
        candidates = sorted(candidates)
        self.recur(candidates, 0, target, [])
        return self.ansList

    def recur(self, cand, d, rem, ans):
        if rem == 0: self.ansList.append(ans)
        if d >= len(cand) or cand[d] > rem:
            return
        for i in range((rem + cand[d]) // cand[d]):
            self.recur(cand, d + 1, rem - i * cand[d], ans + [cand[d]] * i)
