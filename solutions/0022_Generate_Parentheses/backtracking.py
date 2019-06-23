class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recur(p, n, m):
            if n >= 0 and m >= 0:
                # print(p, n, m)
                if n is 0 and m is 0:
                    yield p
                for q in recur(p + '(', n - 1, m + 1): yield q
                for q in recur(p + ')', n, m - 1): yield q
        return list(recur('', n, 0))
