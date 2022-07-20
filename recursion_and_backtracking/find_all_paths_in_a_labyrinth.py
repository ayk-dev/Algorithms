def is_path_possible(r, c, lab):
    if r < 0 or c < 0 or r >= len(lab) or c >= len(lab[0]):
        return False
    if lab[r][c] == '*':
        return False
    if lab[r][c] == 'v':
        return False
    return True


def find_all_exit_paths(r, c, lab, exit_path, direction):
    if not is_path_possible(r, c, lab):
        return

    exit_path.append(direction)

    if lab[r][c] == 'e':
        print(''.join(exit_path))
    else:
        lab[r][c] = 'v'

        find_all_exit_paths(r - 1, c, lab, exit_path, 'U')
        find_all_exit_paths(r + 1, c, lab, exit_path, 'D')
        find_all_exit_paths(r, c - 1, lab, exit_path, 'L')
        find_all_exit_paths(r, c + 1, lab, exit_path, 'R')
        lab[r][c] = '-'
    exit_path.pop()


rows = int(input())
cols = int(input())

labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

find_all_exit_paths(0, 0, labyrinth, [], '')