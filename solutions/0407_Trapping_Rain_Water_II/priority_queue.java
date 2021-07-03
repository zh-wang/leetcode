class Solution {
    public int trapRainWater(int[][] heightMap) {
        int m = heightMap.length;
        int n = (m == 0 ? 0 : heightMap[0].length);
        PriorityQueue<Node> q = new PriorityQueue<>((a, b) -> a.h - b.h);
        int dirs[][] = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
        boolean visited[][] = new boolean[m][n];

        for (int i = 0; i < n; ++i) {
            q.add(new Node(0, i, heightMap[0][i]));
            q.add(new Node(m-1, i, heightMap[m-1][i]));
            visited[0][i] = visited[m-1][i] = true;
        }
        for (int i = 1; i < m-1; ++i) {
            q.add(new Node(i, 0, heightMap[i][0]));
            q.add(new Node(i, n-1, heightMap[i][n-1]));
            visited[i][0] = visited[i][n-1] = true;
        }

        int ret = 0;
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; ++d) {
                int r = dirs[d][0] + cur.r, c = dirs[d][1] + cur.c;
                if (r < 0 || r >= m || c < 0 || c >= n || visited[r][c]) continue;
                ret += Math.max(0, cur.h - heightMap[r][c]);
                q.add(new Node(r, c, Math.max(cur.h, heightMap[r][c])));
                visited[r][c] = true;
            }
        }
        return ret;
    }

    class Node {
        int r;
        int c;
        int h;

        Node(int r, int c, int h) {
            this.r = r;
            this.c = c;
            this.h = h;
        }
    }
}
