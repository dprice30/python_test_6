# The aim of this assignment is to build a basic calculator that can perform 

# addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

def addition(*args):
    return sum(args)

sum = addition(90, 1000, 57, 80, 65)
print(f"Sum = {sum}")

def subtract(a, b):
    return a - b

diff = subtract(45, 97)
print(f"Difference = {diff}")


def subtract(*args):
    if not args:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        return subtract(args[0] - args[1], *args[2:])
diff = subtract(1,2,3,4,5)
print(diff)