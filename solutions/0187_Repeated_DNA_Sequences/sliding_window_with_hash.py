// ⭐️

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        DNA_Mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        key, limit = 0, 4 ** 10
        x, y = set(), {}
        for i in range(len(s)):
            key = (key * 4) + DNA_Mapping[s[i]]
            if i >= 9:
                key %= limit
                if key in x:
                    y[key] = s[i-9:i+1]
                x.add(key)
        return list(y.values())<Paste>
