class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1, n = digits.length;
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] + carry == 10) {
                digits[i] = 0;
                carry = 1;
            } else {
                digits[i] = digits[i] + carry;
                carry = 0;
                break;
            }
        }
        if (carry == 1) {
            int[] newArray = new int[n + 1];
            for (int i = 0; i < n; ++i) {
                newArray[i+1] = digits[i];
            }
            newArray[0] = 1;
            return newArray;
        } else {
            return digits;
        }
    }
}
