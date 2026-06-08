def add_two_numbers() -> int:
    numbers = input("").split(",")
    total = sum(int(n) for n in numbers)
    return total


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
