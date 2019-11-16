class Solution {
    public int countPrimes(int n) {
        boolean[] nonPrime = new boolean[n];
        for (int i = 2; i <= Math.sqrt(n); ++i) {
            for (int j = 2 * i; j < n; j += i) {
                nonPrime[j] = true;
            }
        }
        int ret = 0;
        for (int i = 2; i < n; ++i) {
            if (!nonPrime[i]) ++ret;
        }
        return ret;
    }
}
