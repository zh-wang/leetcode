class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        Map<Integer, Integer> m1 = new HashMap<>();
        Map<Integer, Integer> m2 = new HashMap<>();
        Set<Integer> s = new TreeSet<>();
        List<List<Integer>> ret = new ArrayList<>();
        for (int i = 0; i < buildings.length; ++i) {
            s.add(buildings[i][0]);
            s.add(buildings[i][1]);
        }
        int mappedIndex = 0;
        for (Iterator<Integer> it = s.iterator(); it.hasNext(); ) {
            int x = it.next();
            m1.put(x, mappedIndex);
            m2.put(mappedIndex, x);
            mappedIndex += 1;
        }

        int[] counts = new int[20001];
        for (int i = 0; i < buildings.length; ++i) {
            int start = m1.get(buildings[i][0]);
            int end = m1.get(buildings[i][1]);
            for (int j = start; j < end; ++j) {
                counts[j] = Math.max(counts[j], buildings[i][2]);
            }
        }

        if (mappedIndex == 0) return ret;

        int segStart = 0;
        int segHeight = counts[0];
        for (int i = 1; i < mappedIndex; ++i) {
            if (counts[i] != counts[i-1]) {
                List<Integer> seg = new ArrayList<>();
                seg.add(m2.get(segStart));
                seg.add(segHeight);
                ret.add(seg);
                segStart = i;
                segHeight = counts[i];
            }
        }
        List<Integer> seg = new ArrayList<>();
        seg.add(m2.get(segStart));
        seg.add(segHeight);
        ret.add(seg);

        return ret;
    }
}
