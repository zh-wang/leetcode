class Solution {

    private List<String> ret;
    private int ticketsCnt = 0;

    public List<String> findItinerary(List<List<String>> tickets) {
        this.ticketsCnt = tickets.size();
        Map<String, List<Ticket>> adjs = new HashMap<>();
        for (int i = 0; i < tickets.size(); ++i) {
            String from = tickets.get(i).get(0);
            String to = tickets.get(i).get(1);
            List<Ticket> adjList = adjs.getOrDefault(from, new ArrayList<>());
            adjList.add(new Ticket(from, to));
            adjs.put(from, adjList);
        }

        for (String s : adjs.keySet()) {
            Collections.sort(adjs.get(s));
        }

        for (Ticket t : adjs.get("JFK")) {
            if (ret == null) {
                this.dfs(t, adjs, new ArrayList<>());
            }
        }
        return ret;
    }

    private void dfs(Ticket cur,
                     Map<String, List<Ticket>> adjs,
                     List<String> stack) {
        if (this.ret != null) return;
        if (cur.visited) return;

        // check whether cur is the last ticket
        if (stack.size() == this.ticketsCnt - 1) {
            this.ret = new ArrayList<>(stack);
            this.ret.add(cur.from);
            this.ret.add(cur.to);
            return;
        }

        stack.add(cur.from);
        cur.visited = true;
        for (Ticket t : adjs.getOrDefault(cur.to, new ArrayList<>())) {
            this.dfs(t, adjs, stack);
        }
        cur.visited = false;
        stack.remove(stack.size() - 1);
    }

    private static class Ticket implements Comparable<Ticket> {
        String from;
        String to;
        boolean visited = false;

        public Ticket(String from, String to) {
            this.from = from;
            this.to = to;
        }

        @Override
        public int compareTo(Ticket ticket){
            return to.compareTo(ticket.to);
        }
    }
}
