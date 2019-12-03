import random as rd

def kth_smallest(nums, l, r, k):
    p = rd.randrange(l, r + 1) # partition between index p
    pivot = nums[p]
    nums[p], nums[r] = nums[r], nums[p] # swap pivot to right
    lowest = l
    for i in range(lowest, r + 1):
        if nums[i] < pivot:
            nums[i], nums[lowest] = nums[lowest], nums[i]
            lowest += 1
    nums[r], nums[lowest] = nums[lowest], nums[r]

    if lowest + 1 == k:
        return nums[lowest]
    elif lowest + 1 > k:
        return kth_smallest(nums, l, lowest-1, k)
    else:
        return kth_smallest(nums, lowest+1, r, k)

x = [5,3,4,1,2,9,7,5,3,6,7]
print("sorted x:")
print(sorted(x))
print("")
for i in range(len(x)):
    x = [5,3,4,1,2,9,7,5,3,6,7]
    m = kth_smallest(x, 0, len(x)-1, i+1)
    print(m)
    print(x)
