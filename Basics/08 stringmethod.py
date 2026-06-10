# String Method
# Python provides 47+ built-in string methods in the str class.

# Most Important String Methods (Interview & Practical Use):

# IMP point - STRINGS ARE IMMUTABLE
# Python provides a set of BUILT-IN-Methods that we can use to alter and modify the strings
a = "!!!Khan!! !!!!!!!! Khan!!"
print(len(a))
print(a.upper())  # upper method in string
print(a.lower())  # lower method in string
print(a.rstrip("!")) # rstrip method in string( Removes trailing characters from the right side of the string. and removes specified characters from the end of the string. If no argument is passed, whitespace is removed.
print(a.replace("Khan", "Zahid")) # it will replace string 1 to another.
print(a.split(" ")) # Splits a string into a list.

text = "intorduction to python"
print(text.capitalize()) # capitalize() returns a string with the first letter capitalized and all other letters lowercase

print(a.center(70)) # center(width) returns a centered string of specified width by adding spaces on both sides.
print(a.count("Khan")) #count(value) returns the total occurrences of the specified substring.

text = "Hello.py"
print(text.endswith(".py")) # Returns True if the string ends with the specified suffix, otherwise False.

