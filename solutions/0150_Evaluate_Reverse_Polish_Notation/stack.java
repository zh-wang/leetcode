class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") ||
               token.equals("*") || token.equals("/")) {
                Integer b = stack.pop();
                Integer a = stack.pop();
                if (token.equals("+")) stack.push(a + b);
                if (token.equals("-")) stack.push(a - b);
                if (token.equals("*")) stack.push(a * b);
                if (token.equals("/")) stack.push(a / b);
            } else {
                stack.push(Integer.valueOf(token));
            }
        }
        return stack.pop();
    }
}
