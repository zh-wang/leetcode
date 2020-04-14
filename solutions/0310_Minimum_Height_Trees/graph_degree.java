class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            List<Integer> ret = new ArrayList<>();
            ret.add(0);
            return ret;
        }
        List<List<Integer>> adjs = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            adjs.add(new ArrayList<>());
        }
        int[] cnt = new int[n]; // count degree for each vertex
        for (int[] edge : edges) {
            adjs.get(edge[0]).add(edge[1]);
            adjs.get(edge[1]).add(edge[0]);
            cnt[edge[0]] += 1;
            cnt[edge[1]] += 1;
        }
        List<Integer> leafs = new ArrayList<>();
        boolean[] visited = new boolean[n]; // mark vertex which is visited
        for (int i = 0; i < n; ++i) { // add first loop leafs
            if (cnt[i] == 1) {
                leafs.add(i);
            }
        }
        // repeat when leafs are less or equal than 2, until less than 2 vertices remain
        int remain = n;
        while (leafs.size() >= 2 && remain > 2) {
            for (Integer i : leafs) {
                visited[i] = true;
            }
            remain -= leafs.size();
            Set<Integer> s = new HashSet<>();
            for (Integer i : leafs) {
                for (Integer j : adjs.get(i)) {
                    if (!visited[j]) {
                        s.add(j);
                        cnt[i] -= 1;
                        cnt[j] -= 1;
                    }
                }
            }
            leafs.clear();
            for (Integer j : s) {
                if (cnt[j] <= 1) { // only vertex whose degree is less or equal than 1 can be added
                    leafs.add(j);
                }
            }
        }
        return leafs;
    }
}
