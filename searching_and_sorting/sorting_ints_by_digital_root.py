from random import randrange

START_RANGE = 1
END_RANGE = 1000000


def find_digital_root(n):
    if n == 0:
        return n

    num_as_string = str(n)
    result = 0
    for i in range(0, len(num_as_string)):
        result = (result + int(num_as_string[i])) % 9

    if result == 0:
        return 9
    else:
        return result % 9


def sort_numbers_by_digital_root(nums):
    nums_and_dig_root = {}
    for num in nums:
        nums_and_dig_root[num] = find_digital_root(num)
    for k, v in sorted(nums_and_dig_root.items(), key=lambda kvpt: -kvpt[1]):
        print(k)


numbers = []

for i in range(0, 100):
    numbers.append(randrange(START_RANGE, END_RANGE+1))

sort_numbers_by_digital_root(numbers)
