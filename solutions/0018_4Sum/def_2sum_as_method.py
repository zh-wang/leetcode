class Solution:
    ret_list = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        self.ret_list = []
        i = 0
        j = 0
        n = len(nums) - 2

        if nums[0] * 4 > target:
            return []
        if nums[-1] * 4 < target:
            return []

        while i < n:
            j = i + 1
            while j < n:
                self.SumOf2(nums, i, j, target - nums[i] - nums[j])
                while j < n and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return self.ret_list

    def SumOf2(self, nums, i, j, target):
        l = j + 1
        r = len(nums) - 1
        if nums[l] * 2 > target:
            return
        if nums[r] * 2 < target:
            return
        while l < r:
            total = nums[l] + nums[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                self.ret_list.append([nums[i], nums[j], nums[l], nums[r]])
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                r -= 1
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                l += 1
