from typing import List

def read_integers() -> List[int]:
    integers = []
    line = input("")

    numbers = line.split(",")
    for number in numbers:
        integers.append(int(number))
    return integers

    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
