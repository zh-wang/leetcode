class Solution {

    private List<String> ret;

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return new ArrayList<>();
        }

        Map<Integer, String> dict = new HashMap<>();
        dict.put(2, "abc");
        dict.put(3, "def");
        dict.put(4, "ghi");
        dict.put(5, "jkl");
        dict.put(6, "mno");
        dict.put(7, "pqrs");
        dict.put(8, "tuv");
        dict.put(9, "wxyz");
        dict.put(0, " ");

        ret = new ArrayList<>();
        recur(digits, 0, dict, new Stack<>());
        return ret;
    }

    private void recur(String digits,
                       int index,
                       Map<Integer, String> dict,
                       Stack<Character> stack) {
        if (index >= digits.length()) {
            ret.add(convert(stack));
            return;
        }
        Integer num = Integer.valueOf(digits.charAt(index)) - '0';
        for (char c : dict.get(num).toCharArray()) {
            stack.push(c);
            recur(digits, index + 1, dict, stack);
            stack.pop();
        }
    }

    private String convert(Stack<Character> stack) {
        StringBuilder sb = new StringBuilder();
        for (Character c : stack) {
            sb.append(c);
        }
        return sb.toString();
    }
}
