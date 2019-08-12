# ⭐️
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordList = set(wordList)
        ret = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    ret.extend(k for k in layer[w])
                else:
                    # *** This checking method cause TLE
                    # for ww in wordList:
                    #     if self.isTrans(w, ww):
                    #         newlayer[ww] += [j+[ww] for j in layer[w]]
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]
            wordList -= set(newlayer.keys())
            layer = newlayer
            # print(wordList)
            # print(layer)

        return ret

    # def isTrans(self, wa, wb):
    #     count = 0
    #     for i in range(len(wa)):
    #         if wa[i] != wb[i]:
    #             count += 1
    #     return count == 1
