class Solution {

    private List<String> ret;

    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, List<Integer>> adjs = new HashMap<>();
        for (int i = 0; i < tickets.size(); ++i) {
            List<String> t = tickets.get(i);
            List<Integer> adjList = adjs.getOrDefault(t.get(0), new ArrayList<>());
            int j = 0;
            while (j < adjList.size()
                    && t.get(1).compareTo(
                       tickets.get(adjList.get(j)).get(1)
                    ) > 0
                  ) {
                ++j;
            }
            adjList.add(j, i);
            adjs.put(t.get(0), adjList);
        }

        for (Integer t : adjs.get("JFK")) {
            if (ret == null) {
                dfs(t, new ArrayList<>(), new boolean[tickets.size()], adjs, tickets);
            }
        }
        return ret;
    }

    private void dfs(int tid,
                     List<String> stack,
                     boolean[] visited,
                     Map<String, List<Integer>> adjs,
                     List<List<String>> tickets) {
        if (this.ret != null) return;
        stack.add(tickets.get(tid).get(0));
        visited[tid] = true;
        if (stack.size() == tickets.size()) { // tid is the last ticket
            ret = new ArrayList<>(stack);
            ret.add(tickets.get(tid).get(1));
            return;
        }
        List<Integer> adjList = adjs.get(tickets.get(tid).get(1));
        if (adjList != null) {
            for (Integer nextTicket : adjList) {
                if (!visited[nextTicket]) {
                    dfs(nextTicket, stack, visited, adjs, tickets);
                }
            }
        }
        visited[tid] = false;
        stack.remove(stack.size() - 1);
    }
}
