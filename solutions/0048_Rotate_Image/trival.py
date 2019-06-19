class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            s = i
            t = len(matrix) - 1 - s
            # s,s+0  s,s+1  ...  s,t
            #  ...               s+1,t
            # t-1,s              ...
            # t,s   ...   t,t-1  t,t
            for j in range(t - s):
                temp = matrix[s][s+j] # keep top row
                matrix[s][s+j] = matrix[t-j][s] # top row <- left col
                matrix[t-j][s] = matrix[t][t-j]; # left col <- bot row
                matrix[t][t-j] = matrix[s+j][t] # bot row <- right col
                matrix[s+j][t] = temp # right col <- top row
