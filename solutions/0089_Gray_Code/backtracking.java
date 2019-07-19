class Solution {

    private boolean[] visited;

    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        int total = (int)Math.pow(2, n);
        visited = new boolean[total];

        int num = 0;
        visited[num] = true;
        result.add(0);

        while (true) {
            boolean found = false;
            for (int i = 0; i < n; ++i) {
                int k = num ^ (1 << i);
                if (!visited[k]) {
                    visited[k] = true;
                    found = true;
                    result.add(k);
                    num = k;
                    break;
                }
            }
            if (!found) {
                break;
            }
        }

        return result;
    }
}
