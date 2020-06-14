class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> edges = new ArrayList<>();
        for (int i = 0; i < numCourses; ++i) {
            edges.add(new ArrayList<Integer>());
        }
        int[] inDegrees = new int[numCourses];
        for (int[] e : prerequisites) {
            edges.get(e[1]).add(e[0]);
            inDegrees[e[0]] += 1;
        }

        // store nodes whose inDegree == 0
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; ++i) {
            if (inDegrees[i] == 0) {
                q.add(i);
            }
        }

        int[] ret = new int[numCourses];
        int cnt = 0; // number of nodes visited
        int ri = 0; // index of ret array
        while (!q.isEmpty()) {
            int i = q.poll();
            for (Integer j : edges.get(i)) {
                --inDegrees[j];
                if (inDegrees[j] == 0) {
                    q.add(j);
                }
            }
            ret[ri++] = i;
            ++cnt;
        }

        return cnt == numCourses ? ret : new int[0];
    }
}
