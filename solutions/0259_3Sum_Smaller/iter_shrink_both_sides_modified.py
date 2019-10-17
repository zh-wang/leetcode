class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        nums.sort()
        ret = 0
        for i in range(len(nums)-2):
            a, b = i+1, len(nums)-1
            while (a < b):
                if (nums[a] + nums[b] + nums[i] < target):
                    ret += b - a
                    a += 1
                else:
                    b -= 1
        return ret
