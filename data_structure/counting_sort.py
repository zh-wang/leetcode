def counting_sort(nums):
    k = max(nums) # k is the max value of all input integers
    n = len(nums)
    C = [0 for _ in range(k+1)] # C_i contains number of integers less that i
    B = [0 for _ in range(n)] # the sorted array
    for a in nums: # count number of occurs of integer i
        C[a] += 1
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    print(C)
    for i in range(n-1, -1, -1):
        B[C[nums[i]]-1] = nums[i]
        C[nums[i]] -= 1
    print(B)

counting_sort([3,4,2,1,5,2,3,4,2,1,3])
