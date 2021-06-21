class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ret = []
        for word in words:
            mark = 0b111
            for c in word.lower():
                if c in 'qwertyuiop':
                    mark = mark & 0b001
                if c in 'asdfghjkl':
                    mark = mark & 0b010
                if c in 'zxcvbnm':
                    mark = mark & 0b100
            if mark > 0 and mark & (mark - 1) == 0:
                ret += [word]
        return ret
