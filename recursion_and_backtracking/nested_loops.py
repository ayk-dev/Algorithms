def nesting_loops(idx, n, vector):
    if idx >= n:
        print(*vector, sep=' ')
        return
    for i in range(1, n + 1):
        vector[idx] = i
        nesting_loops(idx + 1, n, vector)


n = int(input())
vector = [0] * n
nesting_loops(0, n, vector)