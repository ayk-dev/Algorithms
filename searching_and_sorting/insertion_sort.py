def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


numbers = insertion_sort([int(x) for x in input().split()])

print(*numbers, sep=' ')