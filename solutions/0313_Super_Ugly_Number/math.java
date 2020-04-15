// same approve as 0264

class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        if (n <= 0) {
            return 0;
        }

        int k = primes.length;
        List<Integer> arr = new ArrayList<>();
        arr.add(1);

        List<Integer> indexList = new ArrayList<>();
        for (int i = 0; i < k; ++i) {
            indexList.add(0);
        }

        List<Integer> temp = new ArrayList<>();
        for (int i = 0; i < n - 1; ++i) {
            int nextVal = Integer.MAX_VALUE;
            temp.clear();
            for (int j = 0; j < k; ++j) {
                int value = primes[j] * arr.get(indexList.get(j));
                temp.add(value);
                nextVal = Math.min(nextVal, value);
            }
            for (int j = 0; j < k; ++j) {
                if (temp.get(j) == nextVal) {
                    indexList.set(j, indexList.get(j) + 1);
                }
            }
            arr.add(nextVal);
        }
        return arr.get(arr.size() - 1);
    }
}
