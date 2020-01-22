class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return [0]
        ret = [nums[0]]
        for i in range(1, len(nums)):
            ret += [ret[-1] * nums[i]]
        # now ret[i] contains nums[0]*nums[1]*...*nums[i]
        tail = 1 # tail will be nums[i-1]*nums[i-2]*...*nums[i+1]
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = tail * (1 if i == 0 else ret[i-1]) # product of ret[i-1] and tail, just the answer we want
            tail *= nums[i]
        return ret
