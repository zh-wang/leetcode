// STAR

public class Solution {
    /*
     * @param edges: a directed graph where each edge is represented by a tuple
     * @return: the number of edges
     */
    public int balanceGraph(int[][] edges) {
        // Write your code here
        Map<Integer, Long> map = new HashMap<>();
        for(int[] t : edges){
            long val1 = map.getOrDefault(t[0], 0L);
            long val2 = map.getOrDefault(t[1], 0L);
            map.put(t[0], val1 - t[2]);
            map.put(t[1], val2 + t[2]);
        }

        List<Long> list = new ArrayList<>();
        for(long val : map.values()){
            if(val != 0) list.add(val);
        }

        if (list.size() == 0) return 0;

        int k = list.size();
        // subsets that sum of all points is zero
        List<Integer> zerosum = new ArrayList<>();
        // dp of subsets
        int[] dp = new int[1 << k];
        Arrays.fill(dp, Integer.MAX_VALUE / 2 - 1);

        // calculate by subsets, from the lowest indexed subsets (0001) to (1111)
        for (int i = 1; i < (1 << k); ++i) {
            int s = 0; // sum of all points in the subset
            int t = 0; // number of points in the subset
            for (int j = 0; j < k; ++j) {
                if ((i >> j & 1) == 1) {
                    s += list.get(j);
                    t += 1;
                }
            }
            if (s == 0) {
                // if t points in a subset, and their sum is zero
                // we can make all of them to 0 by adding t - 1 edges
                dp[i] = t - 1;
                // Otherwise, it can be formed by two subsets, both of them are zero-sum
                // which is stored in zerosum
                for (Integer j : zerosum) {
                    if ((i & j) == j) { // j is a subset of i
                        // then i - j is another subset, which can form i
                        // e.g. i = 1011, j = 1001
                        //      i - j = 0010
                        dp[i] = Math.min(dp[i], dp[j] + dp[i - j]);
                    }
                }
                zerosum.add(i);
            }
        }
        return dp[(1 << k) - 1];
    }
}
