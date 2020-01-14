class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        PriorityQueue<Building> q = new PriorityQueue<Building>((b1, b2) -> {
            return b2.h - b1.h;
        });
        List<List<Integer>> ret = new ArrayList<>();
        if (buildings.length == 0) {
            return ret;
        }
        int tail = buildings[0][0];
        int tailHeight = 0;
        for (int i = 0; i < buildings.length; ++i) {
            while (!q.isEmpty()) { // find a top which is intersect with current building
                if (buildings[i][0] < q.peek().t) break; // found
                // current building's start is further than top's end
                Building top = q.poll();
                if (top.t > tail) {
                    if (tailHeight != top.h) {
                        ret.add(convert(tail, top.h));
                        tailHeight = top.h;
                    }
                    tail = top.t; // update tail
                }
            }

            if (q.size() == 0) { // no such intersection
                if (tail < buildings[i][0]) { // tail is before current building's start
                    ret.add(convert(tail, 0)); // add a zero-height segment
                    tail = buildings[i][0]; // update tail
                }
            } else { // found intersection
                Building top = q.peek();
                if (buildings[i][2] > top.h && buildings[i][0] > tail) {
                    ret.add(convert(tail, top.h));
                    tail = buildings[i][0]; // update tail
                }
            }

            // add current building into q
            Building b = new Building(buildings[i][0], buildings[i][1], buildings[i][2]);
            q.add(b);
        }

        // handle remaining items in q
        while (!q.isEmpty()) {
            Building top = q.poll();
            if (tail < top.t) {
                if (tailHeight != top.h) {
                    ret.add(convert(tail, top.h));
                    tailHeight = top.h;
                }
                tail = top.t;
            }
        }

        // the final zero height segment
        ret.add(convert(tail, 0));

        return ret;
    }


    private List<Integer> convert(int tail, int height) {
        List<Integer> ret = new ArrayList<>();
        ret.add(tail);
        ret.add(height);
        return ret;
    }

    class Building {
        int s;
        int t;
        int h;
        Building(int s, int t, int h) {
            this.s = s;
            this.t = t;
            this.h = h;
        }
    }
}
