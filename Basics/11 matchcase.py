# SYNTAX for Match-Case Statements in Python
match variable:
    case value1:
        # Code to execute if variable matches value1
    case value2:
        # Code to execute if variable matches value2
    case _:
        # Code to execute if variable does not match any of the above cases
        # Default case (optional)
        # # match checks the value of a variable.
# case defines possible matches.
# ("_") acts as the default case (similar to else)

# EXAMPLE
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")

# OUTPUT- Wednesday
