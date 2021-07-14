import queue
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList += [beginWord]
        q = queue.Queue()
        q.put((beginWord, 1))
        visited = set()

        # init pair of words that can transform between
        keyToIndex = collections.defaultdict(list)
        for i, w in enumerate(wordList):
            for k in range(len(w)):
                key = w[:k] + '*' + w[k+1:]
                keyToIndex[key] += [i]

        while not q.empty():
            s, step = q.get()
            if s == endWord:
                return step
            if s in visited:
                continue
            visited.add(s)
            for k in range(len(s)):
                key = s[:k] + '*' + s[k+1:]
                for i in keyToIndex[key]:
                    q.put((wordList[i], step + 1))
        return 0
