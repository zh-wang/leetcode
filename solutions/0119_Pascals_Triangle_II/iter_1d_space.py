class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        combi = [0 for _ in range(34)]
        for n in range(rowIndex + 1):
            combi[n] = 1
            for k in range(n-1, 0, -1):
                combi[k] = combi[k-1] + combi[k]
        return [v for v in combi if v > 0]
