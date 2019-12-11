class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, v in enumerate(nums):
            if v in pos:
                if i - pos[v] <= k:
                    return True
            pos[v] = i
        return False
