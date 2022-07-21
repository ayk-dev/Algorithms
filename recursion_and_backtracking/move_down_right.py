def count_paths(r, c, rows, cols):
    if r >= rows or c >= cols:
        return 0

    if r == rows - 1 and c == cols - 1:
        return 1

    result = 0
    result += count_paths(r, c + 1, rows, cols)
    result += count_paths(r + 1, c, rows, cols)
    return result


rows = int(input())
cols = int(input())

print(count_paths(0, 0, rows, cols))