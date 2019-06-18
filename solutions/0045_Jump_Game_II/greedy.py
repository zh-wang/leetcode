class Solution:
    def jump(self, nums: List[int]) -> int:
        # let s(i) => step to nums[i], s(j) => step to nums[j]
        # if i < j, then s(i) <= s(j)
        # Prove by contradiction, assume that s(i) > s(j):
        # There must be a common parent in both path i and path j,
        # a. If it is positioned before i, we can rebuild both paths from it.
        #    We can repeat above procedure.
        #    Eventually, we can build a path reach i first.
        #    This is the contradiction of s(i) > s(j)
        # b. If it is positioned after i,
        #    Then we can reach i by just 1 step.
        #    This is the contradiction of s(i) > s(j)
        # Therefore, we can calc the max reach for each step by greedy algorithm.
        if len(nums) == 0: return 0
        i, j = 0, 0 # we can read nums from index i to j by 'step' steps
        step = 0
        while j < len(nums) - 1:
            best_reach = 0
            for k in range(i, j + 1): # search the max reach from i to j
                best_reach = max(best_reach, nums[k] + k)
            i = j + 1
            j = best_reach
            step += 1
        return step
