# STAR

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        tokens = re.split('(\D)', input)
        nums = { i: int(tokens[i]) for i in range(0, len(tokens), 2) }
        ops = { i: {'+': operator.add, '-': operator.sub, '*': operator.mul}[tokens[i]] \
               for i in range(1, len(tokens), 2) }

        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                   for i in range(lo, hi) if i&1
                   for a in build(lo, i - 1)
                   for b in build(i + 1, hi)]
        return build(0, len(tokens) - 1)
