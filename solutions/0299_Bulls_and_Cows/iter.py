class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if len(secret) != len(guess):
            return ''
        cnt = [0] * 10
        cnt2 = [0] * 10
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                cnt[int(secret[i])] += 1
                cnt2[int(guess[i])] += 1
        cows = 0
        for i in range(10):
            cows += min(cnt[i], cnt2[i]) if cnt[i] and cnt2[i] else 0
        return '%dA%dB' % (bulls, cows)
