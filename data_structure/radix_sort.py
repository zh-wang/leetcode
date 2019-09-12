def radix_sort(nums):
    m = max(nums)
    n = len(nums)
    step = 1
    while step < m:
        keys = [(a//step)%10 for a in nums]
        counting_sort(keys, nums)
        print(nums)
        step *= 10

def counting_sort(keys, nums):
    n = len(keys)
    C = [0 for _ in range(11)] # O(k) extra space, k = 𝚯(n)
    B = [0 for _ in range(n)] # O(n) extra space
    for a in keys:
        C[a] += 1
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[keys[i]]-1] = nums[i]
        C[keys[i]] -= 1
    for i in range(len(nums)):
        nums[i] = B[i]

radix_sort([109, 209, 301, 333, 102, 103, 55, 3])
