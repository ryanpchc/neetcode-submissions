def reverse_string(input_string: str) -> str:
    reverse_str = ""
    for i in range(len(input_string) - 1, -1, -1):
        reverse_str += input_string[i]
    
    return reverse_str

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
