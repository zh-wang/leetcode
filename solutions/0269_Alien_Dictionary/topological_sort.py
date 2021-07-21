# STAR --Link-- https://www.lintcode.com/problem/892/

from collections import OrderedDict

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        edges = [[False for _ in range(26)] for _ in range(26)]
        stat = [3 for _ in range(26)] # 3 => node not found
        degrees = [0 for _ in range(26)]
        for i in range(len(words) - 1):
            wa, wb = words[i], words[i + 1]
            for j in range(min(len(wa), len(wb))):
                stat[ord(wa[j]) - 97] = 0
                stat[ord(wb[j]) - 97] = 0
                if wa[j] != wb[j]:
                    print(wa[j], wb[j])
                    edges[ord(wa[j]) - 97][ord(wb[j]) - 97] = True
                    degrees[ord(wb[j]) - 97] += 1
                    break

        char_order = OrderedDict()
        isValid = True
        def dfs(index, arr):
            if stat[index] == 2:
                return
            if stat[index] == 1:
                isValid = False
                return
            stat[index] = 1
            char_order[chr(index + 97)] = 1
            for i in range(26):
                if edges[index][i]:
                    dfs(i, arr + [chr(i + 97)])
            print(arr)
            stat[index] = 2

        for i in range(len(degrees)):
            if degrees[i] == 0 and stat[i] == 0:
                dfs(i, [chr(i + 97)])

        return ''.join(list(char_order.keys()))

x = Solution().alienOrder(["wrt","wrf","er","ett","rftt","a","b"])
print(x)
