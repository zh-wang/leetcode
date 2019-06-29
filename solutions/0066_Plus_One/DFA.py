class Solution:
    def isNumber(self, s: str) -> bool:
        DFA = [
            {}, #0 terminal
            {'blank': 1, 'sign': 2, 'digit': 3, 'point': 5}, #1 blank
            {'digit': 3, 'point': 5}, #2 sign
            {'digit': 3, 'point': 4, 'e': 7, 'blank': 10}, #3 digit
            {'digit': 6, 'e': 7, 'blank': 10}, #4 point
            {'digit': 6}, #5 point must followed by digits
            {'digit': 6, 'e': 7, 'blank': 10}, #6 digit after point
            {'sign': 8, 'digit': 9}, #7 e
            {'digit': 9}, #8 sign
            {'digit': 9, 'blank': 10}, #9 digit
            {'blank': 10} #10 blank
        ]
        state = 1
        for c in s:
            key = None
            if c >= '0' and c <= '9':
                key = 'digit'
            if c == ' ':
                key = 'blank'
            if c == '+' or c == '-':
                key = 'sign'
            if c == 'e':
                key = 'e'
            if c == '.':
                key = 'point'
            if key in DFA[state]:
                state = DFA[state][key]
            else:
                state = 0
        return state in [3, 4, 6, 9, 10]
