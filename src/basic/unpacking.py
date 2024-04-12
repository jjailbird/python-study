def print_numbers(a, b, c, d, e):
    print(a, b, c, d, e)

numbers = [1, 2, 3, 4, 5]
print_numbers(*numbers)  # 1 2 3

first, *middle, last = numbers

print(first, middle, last)

def print_name(first_name, last_name):
    print(f'Hello, {first_name} {last_name}')

name_dict = {'last_name': 'Doe', 'first_name': 'John',}

print_name(**name_dict)


