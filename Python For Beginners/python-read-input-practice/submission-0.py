def add_two_numbers() -> int:
    line = input("")
    numbers = line.split(",")
    tot = 0

    for number in numbers:
        tot += int(number)

    return tot


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
