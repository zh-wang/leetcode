class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(2 ** len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & (1<<j):
                    temp.append(nums[j])
            ret.append(temp)
        return ret
