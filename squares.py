

def print_squares(upper_limit):
    for i in range(1, upper_limit+1, 1):
        print(i * i)


def print_squares_of_even(upper_limit):
    for i in range(2, upper_limit, 2):
        print(i * i)


def print_squares_in_reverse(upper_limit):
    for i in range(upper_limit, 0, -1):
        print(i * i)


print_squares(10)
print_squares_of_even(10)
print_squares_in_reverse(10)
