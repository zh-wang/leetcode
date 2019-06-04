class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;

        char[] chars = s.toCharArray();
        int rowmax = numRows * 2 - 2; // number of rows
        StringBuilder sb = new StringBuilder();

        // first row
        for (int j = 0; j < chars.length; j += rowmax) {
            sb.append(chars[j]);
        }

        // rows in the middle
        for (int i = 1; i < numRows - 1; ++i) {
            for (int j = 0; j < chars.length; j += rowmax) {
                if (j + i < chars.length) {
                    sb.append(chars[j + i]);
                }
                if (j + rowmax - i < chars.length) {
                    sb.append(chars[j + rowmax - i]);
                }
            }
        }

        // last row
        for (int j = numRows - 1; j < chars.length; j += rowmax) {
            sb.append(chars[j]);
        }

        return sb.toString();
    }
}
