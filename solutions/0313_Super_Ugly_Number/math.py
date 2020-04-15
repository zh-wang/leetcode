# same approve as 0264

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n <= 0:
            return 0
        k = len(primes)
        indice = [0] * k
        arr = [1]
        for i in range(n - 1):
            next_vals = [primes[j] * arr[indice[j]] for j in range(k)]
            next_val = min(next_vals)
            for j in range(k):
                if next_vals[j] == next_val:
                    indice[j] += 1
            arr += [next_val]
        return arr[-1]
