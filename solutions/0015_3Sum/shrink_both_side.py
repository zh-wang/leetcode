class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        i = 0
        n = len(nums)
        while i < n - 2:
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
            while i < n - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ret
