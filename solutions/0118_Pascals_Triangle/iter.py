class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ret = [[1], [1, 1]]
        for _ in range(2, numRows):
            arr = ret[-1]
            ret.append( [1] + [arr[i] + arr[i+1] for i in range(len(arr) - 1)] + [1] )
        return ret
