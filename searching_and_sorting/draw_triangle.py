class NumberCannotBeNegative(Exception):
    pass


def get_triangle(n):
    triangle = (n) * ' ' + '#' + '\n'
    for row in range(1, n, 2):
        triangle += (' ' * (n - row) + '$ ')
        triangle += ('$ ' * row + ' ' * (n - row) + '\n')

        if row != n - 1:
            triangle += (' ' * (n - row - 1) + '# ')
            triangle += ('# ' * (row + 1) + ' ' * (n - row) + '\n')
    return triangle


try:
    n = int(input("Enter a positive number: "))
    if n <= 0:
        raise NumberCannotBeNegative("Number must greater than 0, please try again")
    print(get_triangle(n))
except ValueError:
    print("Number must be an integer")







