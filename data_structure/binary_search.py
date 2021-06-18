def find_exact(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] > target:
            r = m
        elif arr[m] < target:
            l = m + 1
        else:
            return l
    return l

# find index of an element's first occurance position, which is greater than target
def find_lower_bound(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] > target:
            r = m
        else:
            l = m + 1
    return l

# find index of an element's first occurance position, which is lesser than target
def find_upper_bound(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] >= target:
            r = m
        else: # m maybe the answer
            if arr[m + 1] >= target:
                return m
            else:
                l = m + 1
    return l

def bs_upper_bound(arr, target):
    k = len(arr)
    first = 0
    while k > 0:
        half = k // 2
        m = first + half
        if arr[m] >= target:
            k = half
        else:
            first = m
            k -= half + 1
    return first

def binary_search_k(arr, target):
    k = len(arr)
    first = 0
    while k > 0:
        half = k // 2
        m = first + half
        if arr[m] >= target:
            k = half
        else:
            first = m + 1
            k -= half + 1
    return first

def debug(func=None):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(ret)
    return wrapper

@debug
def test(func, arr, target, expect_index):
    ret = func(arr, target)
    if expect_index != ret:
        return '{} {} ({}) | Failed. index {} != {}'.format(func.__name__, arr, target, ret, expect_index)
    else:
        return '{} {} ({}) | Passed.'.format(func.__name__, arr, target)

arr = [2, 4, 6]
test(binary_search_k, arr, 4, 1)
test(binary_search_k, arr, 5, 2)
test(binary_search_k, arr, 6, 3)

#      0  1  2  3  4  5  6  7  8  9 10 11 12  13
arr = [1, 1, 2, 2, 2, 3, 3, 5, 6, 9, 9, 9, 9, 10]
test(find_exact, arr, 10, 13)

test(find_lower_bound, arr, 9, 13)
test(find_lower_bound, arr, 8, 9)
test(find_lower_bound, arr, 4, 7)
test(find_lower_bound, arr, 2, 5)

arr = [2, 5, 5, 5, 5, 6]
test(find_lower_bound, arr, 4, 1)
test(find_lower_bound, arr, 5, 5)

arr = [1,3,6,10,15]
test(find_lower_bound, arr, 4, 2)

#      0  1  2  3  4  5  6  7  8  9  10 11 12 13
arr = [1, 1, 2, 2, 2, 3, 3, 5, 6, 9, 9, 9, 9, 10]
test(find_upper_bound, arr, 5, 6)
test(find_upper_bound, arr, 6, 7)
test(find_upper_bound, arr, 9, 8)
test(find_upper_bound, arr, 2, 1)
test(bs_upper_bound, arr, 5, 6)
test(bs_upper_bound, arr, 6, 7)
test(bs_upper_bound, arr, 9, 8)
test(bs_upper_bound, arr, 2, 1)
