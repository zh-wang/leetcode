class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret = []
        marks = [False for _ in range(n)]
        self.recur(marks, [], 0, k, 0)
        return self.ret

    def recur(self, marks, arr, s, k, d):
        if d >= k:
            self.ret.append(arr[:])
            return
        for i in range(s, len(marks)):
            if not marks[i]:
                marks[i] = True
                self.recur(marks, arr + [i+1], i+1, k, d+1)
                marks[i] = False
