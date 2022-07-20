def gen01vectors(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        gen01vectors(idx + 1, vector)


n = int(input())
vector = [0] * n
gen01vectors(0, vector)