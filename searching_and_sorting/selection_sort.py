def selections_sort(nums):
    for idx in range(len(nums)):
        min_number = nums[idx]
        min_idx = idx
        for next_idx in range(idx + 1, len(nums)):
            next_num = nums[next_idx]
            if next_num < min_number:
                min_number = next_num
                min_idx = next_idx
        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
    return nums


numbers = selections_sort([int(x) for x in input().split()])

print(*numbers, sep=' ')
