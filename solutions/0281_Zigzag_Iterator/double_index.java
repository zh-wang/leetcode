// --Link--
// https://www.lintcode.com/problem/zigzag-iterator/description

public class ZigzagIterator {

    private int i1 = 0;
    private int i2 = 0;
    private List<Integer> v1;
    private List<Integer> v2;

    /*
    * @param v1: A 1d vector
    * @param v2: A 1d vector
    */
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        // do intialization if necessary
        this.v1 = v1;
        this.v2 = v2;
    }

    /*
     * @return: An integer
     */
    public int next() {
        // write your code here
        if (i1 >= v1.size() && i2 >= v2.size()) {
            return 0;
        }
        if (i1 >= v1.size()) {
            return v2.get(i2++);
        }
        if (i2 >= v2.size()) {
            return v1.get(i1++);
        }
        if (i1 == i2) {
            return v1.get(i1++);
        } else {
            return v2.get(i2++);
        }
    }

    /*
     * @return: True if has next
     */
    public boolean hasNext() {
        // write your code here
        if (i1 >= v1.size() && i2 >= v2.size()) {
            return false;
        }
        return true;
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator solution = new ZigzagIterator(v1, v2);
 * while (solution.hasNext()) result.add(solution.next());
 * Output result
 */
