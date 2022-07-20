fibonacci_cache = {}


def get_fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 1:
        value = 1
    else:
        value = get_fibonacci(n - 1) + get_fibonacci(n - 2)
    fibonacci_cache[n] = value
    return value


n = int(input())
print(get_fibonacci(n))
