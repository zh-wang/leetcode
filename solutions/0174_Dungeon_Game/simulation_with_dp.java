class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length();
        int n = dungeon[0].length();
        int encounter[] = new int[n+1];
        int life[] = new int[n+1]; // we want this as low as possible
        for (int j = 0; j < n+1; ++j) {
            encounter[j] = Integer.MIN_VALUE;
            life[j] = Integer.MAX_VALUE;
        }
        for (int i = 1; i < m+1; ++i) {
            encounter[0] = Integer.MIN_VALUE;
            life[0] = Integer.MAX_VALUE;
            for (int j = 1; j < n+1; ++j) {jjj
                if (life[j-1] < life[j]) {
                    life[j] = life
                }
            }
        }
    }
}
