# Given a pattern P􏰀, the prefix function for the pattern P is the function
# π : {0, 1, 2, ... , m} -> {0, 1, ... , m-1} such that
# π[q] = max { k: k < q and P_k is suffix of P_q }
def kmp_lookup_table(s):
    k = 0
    pi = [0] * len(s)
    for i in range(1, len(s)):
        # if we failed matching index i - 1, we can match again at pi[i - 1]
        # try to find where s[i] == s[k].
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        # if we can find t which s[i] == s[k]
        # then if we failed matching index i, we can match again from k+1
        if s[i] == s[k]:
            k += 1
        pi[i] = k
        print(pi)
    return pi

# pi = kmp_lookup_table('cacacabc')

def kmp_matching(s, p):
    n, m = len(s), len(p)
    pi = kmp_lookup_table(p)
    q = 0 # number of character matched
    for i in range(n):
        while q > 0 and s[i] != p[q]:
            q = pi[q - 1]
        if s[i] == p[q]:
            q += 1
        if q == m:
            print("%s[%s]%s" % (s[:i-q+1], s[i-q+1:i+1], s[i+1:]))
            q = pi[q - 1]

kmp_matching("cabwacacacabcxfeacaca_wecacacacacabcweasdf", "cacacabc")
