// TLE

class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        int best = 0;
        for (Integer pHouse : houses) {
            int cBest = Integer.MAX_VALUE;
            for (Integer pHeater : heaters) {
                cBest = Math.min(cBest, Math.abs(pHouse - pHeater));
            }
            best = Math.max(best, cBest);
        }
        return best;
    }
}
