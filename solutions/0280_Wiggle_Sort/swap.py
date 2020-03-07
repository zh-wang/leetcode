class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        for i in range(1, len(nums), 2):
            if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            if i + 1 < len(nums):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        print(nums)

Solution().wiggleSort([5,3,2,6,1,7,0,10,22,8,9])
