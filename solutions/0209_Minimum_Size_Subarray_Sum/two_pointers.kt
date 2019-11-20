// STAR

class Solution {
    fun minSubArrayLen(s: Int, nums: IntArray): Int {
        if (nums.size == 0) return 0
        var sum = 0
        var start = 0
        var ret = nums.size
        for (i in 0..nums.size-1) {
            sum += nums[i]
            while (sum >= s) {
                ret = Integer.min(ret, i - start + 1)
                sum -= nums[start++]
            }
        }
        return ret
    }
}
