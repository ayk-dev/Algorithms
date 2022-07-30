def merge_arrays(left, right):
    res = [None] * (len(left) + len(right))

    left_idx = 0
    right_idx = 0
    res_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res[res_idx] = left[left_idx]
            left_idx += 1
        else:
            res[res_idx] = right[right_idx]
            right_idx += 1
        res_idx += 1

    while left_idx < len(left):
        res[res_idx] = left[left_idx]
        left_idx += 1
        res_idx += 1

    while right_idx < len(right):
        res[res_idx] = right[right_idx]
        right_idx += 1
        res_idx += 1

    return res


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left = nums[:mid_idx]
    right = nums[mid_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = [int(x) for x in input().split()]

result = merge_sort(numbers)

print(*result, sep=' ')