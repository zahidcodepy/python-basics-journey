# SYNTAX
# for variable in sequence:
     # code block to be executed

# LET'S SEE AN EXAMPLE
language = "PYTHON"
for i in language:
    print(i)
# In this example, we have a string "PYTHON". The for loop iterates over each character in the string and prints it.
# The variable 'i' takes on the value of each character in the string during each iteration of the loop.
# The output of the above code will be:
# P
# Y
# T
# H
# O
# N

# Using range() Function
# The range() function is commonly used in for loops to generate a sequence of numbers. It can take one, two, or three arguments:

# Syntax:

# range(stop)
# range(start, stop)
# range(start, stop, step)

# Example1: Basic usage with One Argument - Stop
for x in range(5):
    print(x)
# Output: 0 1 2 3 4
# Example2: Basic usage with Start, Stop and Step
for y in range(1, 10, 2):
    print(y)
# Output: 1 3 5 7 9
