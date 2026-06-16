# Functions in Python.
# A function is a block of code that performs a specific task.

# Basic Concepts:
# • Create function: Use the def keyword to define a function.
# • Call function: Use the function's name followed by () to run it.
# • Parameter: The variable listed inside parentheses in function definition.
# • Argument: The actual value you pass to function when you call it.

# SYNTAX

# def function_name(parameters):
    # code block to be executed
    # return value (optional)


# EXAMPLE

def greet(name): # 'name' is a parameter of the function 'greet'
    print("Hello, " + name +" Welcome to the world of Python!") # this line will print the greeting message
    return "Greeting sent to " + name  # This line will return a string       

# Calling the function
result = greet("KHAN")  
print(result)

# In this example, we define a function called 'greet' that takes one parameter 'name'.
