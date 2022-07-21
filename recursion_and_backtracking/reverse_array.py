def reverse_recursion(idx, arr):

    if idx == (len(arr) // 2):
        return

    arr[idx], arr[len(arr) - 1 - idx] = arr[len(arr) - 1 - idx], arr[idx]
    reverse_recursion(idx + 1, arr)


array = input().split()
reverse_recursion(0, array)

print(' '.join(array))
