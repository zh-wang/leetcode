# --STAR--

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        i, j, k = 0, 0, 0
        arr = [1]
        while len(arr) < n:
            m2 = arr[i] * 2
            m3 = arr[j] * 3
            m5 = arr[k] * 5
            nextVal = min(m2, m3, m5)
            if m2 == nextVal:
                i += 1
            if m3 == nextVal:
                j += 1
            if m5 == nextVal:
                k += 1
            arr += [nextVal]
        return arr[-1]
