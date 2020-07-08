class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = collections.Counter(nums)
        result = [[]]
        for v in sorted(counts.keys()):
            result = [pre + [v] * repeat for pre in result for repeat in range(counts[v]+1)]
        return result<Paste>
