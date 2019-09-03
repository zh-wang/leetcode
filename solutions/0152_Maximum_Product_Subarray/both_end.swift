// ⭐️
class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        if (nums.count == 0) {
            return 0
        }
        // Suppose nums contains P,P,N,P,N,P,P,N,P (P=>positive, N=>negative)
        // The answer will be    |-----------|
        //   or                        |---------|
        // So we can calc the product from both end, then take max
        // If nums contains 0, we can reset that from point
        var best = nums[0]
        var l = 0, r = 0, n = nums.count // l & r are product from both end
        for i in 0..<n {
            // l is 0 means the first step or after being multiplied by 0
            l = l == 0 ? nums[i] : nums[i] * l
            r = r == 0 ? nums[n - i - 1] : nums[n - i - 1] * r
            best = max(best, l, r)
        }
        return best
    }
}
