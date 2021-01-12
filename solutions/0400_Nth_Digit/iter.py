class Solution:
    def findNthDigit(self, n: int) -> int:
        lenOfNum = 1
        totalNum = 9
        # total digits for len=1 number [1, 2, ... , 9] (9 numbers) is 9
        # total digits for len=2 number [10, 11, ... ,99] (90 numbers) is the count of numbers in the range * lenOfNum
        # this holds for len=n
        while n > totalNum * lenOfNum:
            n -= totalNum * lenOfNum
            lenOfNum += 1
            totalNum *= 10
        p = (n - 1) // lenOfNum # offset from the first len=lenOfNum number, which is totalNum // 9
        q = (n - 1) % lenOfNum # the index of digit
        return self.kthDigitSignificant(totalNum // 9 + p, q)

    def kthDigitSignificant(self, n, k):
        arr = []
        while n > 0:
            arr += [n % 10]
            n //= 10
        return arr[-(k + 1)]
