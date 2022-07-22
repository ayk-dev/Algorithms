def bubble_sort(nums):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for idx in range(1, len(nums) - counter):
            if nums[idx] < nums[idx - 1]:
                nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
                is_sorted = False
        counter += 1

    return nums


numbers = bubble_sort([int(x) for x in input().split()])

print(*numbers, sep=' ')

# 3 5 1 2 4 6