def cal_array_sum(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + cal_array_sum(numbers, index + 1)


numbers = [int(x) for x in input().split()]
print(cal_array_sum(numbers, 0))