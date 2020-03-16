# --Link--
# https://www.lintcode.com/problem/unique-word-abbreviation/description

class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.mydic = set(dictionary)
        abbs = [v if len(v) <= 2 else v[0] + str(len(v) - 2) + v[-1] for v in self.mydic]
        self.abb2Cnt = collections.Counter(abbs)

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        if abb in self.abb2Cnt:
            return word in self.mydic and self.abb2Cnt[abb] == 1
        return True

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)
