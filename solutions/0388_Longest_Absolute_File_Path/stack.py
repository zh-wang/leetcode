from functools import reduce

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split('\n')
        if not arr:
            return 0

        def numOfTabs(f):
            return len(f) - len(f.replace('\t', ''))

        def totalLength(sk):
            return reduce(lambda x, y: x + len(y.replace('\t', '')), sk, 0) + len(sk) - 1

        sk = [arr[0]]
        best = totalLength(sk) if '.' in arr[0] else 0

        for f in arr[1:]:
            c_tabs, p_tabs = numOfTabs(f), numOfTabs(sk[-1])
            if c_tabs == p_tabs + 1:
                sk += [f]
            else:
                while sk and p_tabs >= c_tabs:
                    sk.pop()
                    if not sk:
                        break
                    p_tabs = numOfTabs(sk[-1])
                sk += [f]
            if '.' in f:
                best = max(best, totalLength(sk))

        return best
