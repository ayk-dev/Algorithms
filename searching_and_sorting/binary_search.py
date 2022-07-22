def find_target_binary(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        if nums[mid_idx] == target:
            return mid_idx

        if nums[mid_idx] < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]

target = int(input())

print(find_target_binary(nums, target))


