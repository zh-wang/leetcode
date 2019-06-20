class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = collections.defaultdict(list)
        for s in strs:
            ret[tuple(sorted(s))].append(s)
        return list(ret.values())
