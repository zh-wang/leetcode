// ⭐️
import javafx.util.Pair;

class Solution {
    public int ladderLength(String beginWord, String endWord,
                            List<String> wordList) {

        wordList.add(0, beginWord);
        // a map contains *-string and index of word in wordList
        // e.g. h*t => [1(hot), 2(hat)]
        // The time complexity on original matching is O(KN^2)
        // By utilizing this map, it takes O(KN) for init,
        // and in BFS, it takes O(K) for matching.
        Map<String, List<Integer>> map = new HashMap<>();
        int k = beginWord.length();
        for (int i = 0; i < wordList.size(); ++i) {
            String s = wordList.get(i);
            for (int j = 0; j < k; ++j) {
                String target = s.substring(0, j) + "*" + s.substring(j+1);
                List<Integer> indice = map.getOrDefault(target,
                                                        new ArrayList<>());
                indice.add(i);
                map.put(target, indice);
            }
        }

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
            for (int j = 0; j < k; ++j) {
                String target = curWord.substring(0, j) + "*" +
                    curWord.substring(j+1);
                for (Integer i : map.getOrDefault(target, new ArrayList<>())) {
                    q.add(new Pair<Integer, Integer>(i, step+1));
                }
            }
        }
        return 0;
    }
}
