nums = [1,1,3]
checked = [False] * len(nums)
ret = []

def perm(nums, arr, ret):
    if len(arr) >= len(nums):
        ret += [arr[:]]
        return
    for i in range(len(nums)):
        if not checked[i]:
            checked[i] = True
            perm(nums, arr + [nums[i]], ret)
            checked[i] = False

perm(nums, [], ret)
print(ret)

def permUniq(nums, arr, pos, ret):
    if len(arr) >= len(nums):
        ret += [arr[:]]
        return
    for i in range(len(nums)):
        if not checked[i]:
            if len(arr) > 0:
                if nums[i] == arr[-1] and i <= pos[-1]:
                    continue
            checked[i] = True
            permUniq(nums, arr + [nums[i]], pos + [i], ret)
            checked[i] = False

ret = []
permUniq(nums, [], [], ret)
print(ret)

