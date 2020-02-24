class Solution {

    var checked = booleanArrayOf()
    var ret = mutableListOf<List<Int>>()

    fun permuteUnique(nums: IntArray): List<List<Int>> {
        var arr = intArrayOf()
        checked = BooleanArray(nums.size)
        nums.sort()
        permUnit(nums, arr)
        return ret
    }

    fun permUnit(nums: IntArray, arr: IntArray) {
        if (arr.size >= nums.size) {
            ret.add(arr.toList())
            return
        }
        for (i in 0..nums.size - 1) {
            if (checked[i]) continue;
            // remove duplicates
            if (i > 0 && nums[i-1] == nums[i] && !checked[i-1]) continue
            checked[i] = true
            permUnit(nums, arr + intArrayOf(nums[i]))
            checked[i] = false
        }
    }
}
