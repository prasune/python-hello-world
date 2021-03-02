# no overloading allowed in python


def print_table(num=5, start=1, end=10):
    for i in range(start, end+1, 1):
        print(f"{num} * {i} = {num*i}")


print_table()
print_table(1)
print_table(20, 31, 40)


def sum_of_two_nums(num1, num2):
    sum_of_nums = num1 + num2
    return sum_of_nums


print(sum_of_two_nums(5, 6))
