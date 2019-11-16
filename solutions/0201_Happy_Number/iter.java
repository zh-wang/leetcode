class Solution {
    public boolean isHappy(int n) {
        Set<Integer> visited = new HashSet<>();
        int k = n;
        while (!visited.contains(k)) {
            if (k == 1) return true;
            visited.add(k);
            int nextK = 0;
            while (k > 0) {
                int t = k % 10;
                nextK += t * t;
                k /= 10;
            }
            k = nextK;
        }
        return false;
    }
}
