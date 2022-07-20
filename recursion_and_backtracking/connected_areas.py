class Area():
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def traverse_area(r, c, matrix):
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
        return 0
    if matrix[r][c] != '-':
        return 0

    matrix[r][c] = 'v'

    result = 1
    result += traverse_area(r + 1, c, matrix)
    result += traverse_area(r - 1, c, matrix)
    result += traverse_area(r, c + 1, matrix)
    result += traverse_area(r, c - 1, matrix)

    return result


rows = int(input())
cols = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []
for i in range(rows):
    for j in range(cols):
        result = traverse_area(i, j, matrix)
        if result != 0:
            areas.append(Area(i, j, result))

print(f'Total areas found: {len(areas)}')
sorted_areas = sorted(areas, key=lambda a: a.size, reverse=True)
for idx, area in enumerate(sorted_areas):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')