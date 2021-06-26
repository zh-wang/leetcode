# STAR

class Solution:
    ret = []

    def convert(self, word, index_seq):
        '''
        convert list of index into abbreviation without recursion
        '''
        r1, r2 = [], []
        pi = 0
        mark = True
        for i in index_seq:
            if mark:
                r1.append( word[pi:i] )
                r2.append( i - pi )
            else:
                r2.append( word[pi:i] )
                r1.append( i - pi )
            pi = i
            mark = not mark
        return (r1, r2)

    def convert2(self, word, index_seq, s):
        '''
        convert list of index into abbreviation with recursion
        '''
        if s >= len(index_seq):
            return ([], [])
        k = self.convert2(word, index_seq, s + 1)
        pa = index_seq[s]
        pb = index_seq[s - 1] if s > 0 else 0
        return ( [word[pb:pa]] + k[1], [pa - pb] + k[0] )

    def arr_to_str(self, arr):
        return ''.join(map(str, arr))

    def recur2(self, word, start, index_seq):
        '''
        build a list of index to seperate chars
        '''
        if start >= len(word):
            self.ret += [index_seq[:]]
            return
        for i in range(start + 1, len(word) + 1):
            self.recur2(word, i, index_seq + [i])

    def test(self, word):
        self.word_abbr(word, 0, [], [])
        print(self.ret)
        # self.recur2(word, 0, [])
        # r1 = []
        # r2 = []
        # for arr in self.ret:
            # g = self.convert(word, arr)
            # h = self.convert2(word, arr, 0)
            # print(g, h)
            # r1 += [self.arr_to_str(g[0]), self.arr_to_str(g[1])]
            # r2 += [self.arr_to_str(h[0]), self.arr_to_str(h[1])]
        # r1.sort()
        # r2.sort()
        # print(r1)
        # print(r2)

    # ===================

    def shortest_word_abbr(self, word, dictionary):
        self.word_abbr(word, 0, [], [])
        shortest_abbrs = sorted(self.ret, key = lambda x : self.length_of_abbr(x))
        for abbr in shortest_abbrs:
            ok = True
            for w in dictionary:
                if self.is_abbr_valid(abbr, w):
                    ok = ok and False
            if ok:
                return abbr
        return 'NO ANSWER'

    def length_of_abbr(self, abbr):
        return len(''.join(map(str, abbr)))

    def word_abbr(self, word, start, a, b):
        '''
        result list a contains abbreviations which end with char
        result list b contains abbreviations which end with number
        exchange a and b in each recursion
        '''
        if start >= len(word):
            self.ret += [a[:]]
            self.ret += [b[:]]
        for i in range(start + 1, len(word) + 1):
            self.word_abbr(word, i, b + [word[start:i]], a + [i-start])

    def is_abbr_valid(self, abbr, word):
        i = 0
        for v in abbr:
            if type(v) is int:
                i += v
            if type(v) is str:
                if word[i : i + len(v)] != v:
                    return False
                i += len(v)
        if i == len(word):
            return True
        return False

x = Solution().shortest_word_abbr("apple", ["plain", "amber", "blade"])
print(x)

