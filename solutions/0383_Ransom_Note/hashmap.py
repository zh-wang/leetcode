from collections import Counter
from functools import reduce

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        mag_dict = Counter(magazine)
        return all([k in mag_dict and v <= mag_dict[k] for k, v in ransom_dict.items()])
