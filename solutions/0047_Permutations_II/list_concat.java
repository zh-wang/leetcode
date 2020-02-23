class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        ret.add(new ArrayList<Integer>());
        for (int i = 0; i < nums.length; ++i) {
            List<List<Integer>> new_ret = new ArrayList<>();
            for (List<Integer> l : ret) {
                for (int j = 0; j < l.size() + 1; ++j) {
                    List<Integer> pa = new ArrayList<>(l.subList(0, j));
                    List<Integer> pb = new ArrayList<>(l.subList(j, l.size()));
                    List<Integer> center = List.of(nums[i]); // java 9
                    new_ret.add( merge(pa, center, pb) );
                    if (j < l.size() && nums[i] == l.get(j)) {
                        break;
                    }
                }
            }
            ret = new_ret;
        }
        return ret;
    }


    public static <T> List<T> merge(List<T>... args) {
        final List<T> result = new ArrayList<>();

        for (List<T> list : args) {
            result.addAll(list);
        }

        return result;
    }
}
