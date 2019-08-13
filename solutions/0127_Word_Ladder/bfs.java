import javafx.util.Pair;

class Solution {
    public int ladderLength(String beginWord, String endWord,
                            List<String> wordList) {
        wordList.add(0, beginWord);
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        q.add(new Pair<Integer, Integer>(0, 1));
        boolean[] visited = new boolean[wordList.size()];
        while (!q.isEmpty()) {
            Pair<Integer, Integer> pair = q.poll();
            int curIndex = pair.getKey();
            if (visited[curIndex]) continue;
            String curWord = wordList.get(pair.getKey());
            int step = pair.getValue();
            if (curWord.equals(endWord)) {
                return step;
            }
            visited[curIndex] = true;
            for (int i = 0; i < wordList.size(); ++i) {
                if (!visited[i] && canTrans(curWord, wordList.get(i))) {
                    q.add(new Pair<Integer, Integer>(i, step+1));
                }
            }
        }
        return 0;
    }

    private boolean canTrans(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); ++i) {
            count += a.charAt(i) == b.charAt(i) ? 0 : 1;
        }
        return count == 1;
    }
}
