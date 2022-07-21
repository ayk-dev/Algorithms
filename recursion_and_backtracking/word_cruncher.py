def find_all_solutions(idx, target, words_by_idx, words_count, used_words):
    if idx >= len(target):
        print(' '.join(used_words))
    if idx not in words_by_idx:
        return

    for w in words_by_idx[idx]:
        if words_count[w] == 0:
            continue
        used_words.append(w)
        words_count[w] -= 1

        find_all_solutions(idx + len(w),target, words_by_idx, words_count, used_words)

        used_words.pop()
        words_count[w] += 1


words = input().split(', ')
target = input()

words_by_idx = {}
words_count = {}

for w in words:
    if w in words_count:
        words_count[w] += 1
        continue

    words_count[w] = 1

    try:
        idx = 0
        while True:
            idx = target.index(w, idx)
            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(w)
            idx += len(w)
    except ValueError:
        pass

find_all_solutions(0, target, words_by_idx, words_count, [])