class Solution:
    def totalNQueens(self, n: int) -> int:
        # 1. column check
        # if coloumn i is occupied, add i into cols
        # 2. diagonal check
        # if row m, col n is occupied, add m+n into pos_k, add m-n into neg_k
        self.cols = set()
        self.pos_k = set()
        self.neg_k = set()
        self.ret = 0
        self.recur(n, 0)
        return self.ret

    def recur(self, n, d):
        if d >= n:
            self.ret += 1
            return
        for i in range(n):
            if i not in self.cols and d - i not in self.neg_k and d + i not in self.pos_k:
                self.cols.add(i)
                self.neg_k.add(d - i)
                self.pos_k.add(d + i)
                self.recur(n, d + 1)
                self.cols.remove(i)
                self.neg_k.remove(d - i)
                self.pos_k.remove(d + i)
