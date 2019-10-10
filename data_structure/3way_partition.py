import random as rd

def p3(nums):
    i, j = 0, 0
    n = len(nums)-1
    median = 2
    while j <= n:
        if nums[j] < median:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j+1
        elif nums[j] > median:
            nums[j], nums[n] = nums[n], nums[j]
            n -= 1
        else:
            j += 1

x = [1,1,2,3,3,2,1,1,2,1]
rd.shuffle(x)
p3(x)
print(x)
