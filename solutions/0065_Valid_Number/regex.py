import re
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.fullmatch('([-+]?[0-9]*\.?[0-9]+|[-+]?[0-9]+\.?[0-9]*){1}(e[-+]?[0-9]+)?', s.strip()) is not None
