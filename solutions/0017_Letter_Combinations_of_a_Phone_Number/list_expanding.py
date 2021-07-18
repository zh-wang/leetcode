# STAR

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ret = [[]]
        for i in range(len(digits)):
            newRet = []
            for numList in ret:
                for c in numToChar[digits[i]]:
                    newRet.append(numList + [c])
            ret = newRet
        return [''.join(numList) for numList in ret]
