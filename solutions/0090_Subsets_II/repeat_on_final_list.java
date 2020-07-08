class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int v : nums) {
            count.put(v, count.getOrDefault(v, 0) + 1);
        }

        List<List<Integer>> ret = new ArrayList<>();
        ret.add(new ArrayList<>());
        if (count.size() == 0) {
            return ret;
        }
        List<Integer> keys = new ArrayList<>(count.keySet());
        Collections.sort(keys);

        for (int v : keys) {
            List<List<Integer>> newRet = new ArrayList<>();
            int repeat = count.get(v);
            for (var list : ret) {
                for (int r = 0; r <= repeat; ++r) {
                    newRet.add(genListByRepeat(list, v, r));
                }
            }
            ret = newRet;
        }
        return ret;
    }

    private List<Integer> genListByRepeat(List<Integer> list, int v, int repeat) {
        List<Integer> ret = new ArrayList<>(list);
        for (int i = 0; i < repeat; ++i) {
            ret.add(v);
        }
        return ret;
    }
}
