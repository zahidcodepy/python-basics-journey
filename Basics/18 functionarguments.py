"""Function arguments in Python:
  
Learn how to pass arguments to Python functions.

A parameter is the name in a function definition.
An argument is the value passed when the function is called.

    def greet(name):       # name is a parameter
        return f"Hi, {name}"

    greet("Ari")           # "Ari" is an argument
"""


# 1. Positional arguments match parameters from left to right.
def add(first_number, second_number):
	return first_number + second_number


print("Positional:", add(2, 3))


# 2. Keyword arguments use parameter names, so their order can change.
def describe_person(name, age):
	return f"{name} is {age} years old."


print("Keyword:", describe_person(age=30, name="Ari"))


# 3. A default value is used when an argument is not provided.
def power(number, exponent=2):
	return number**exponent


print("Default:", power(4))
print("Custom exponent:", power(4, 3))


# Avoid mutable defaults such as items=[].
# A default list would be shared by every call.
def add_item(item, items=None):
	if items is None:
		items = []

	items.append(item)
	return items


print("New lists:", add_item("apple"), add_item("banana"))


# 4. *args collects extra positional arguments into a tuple.
def total(*numbers):
	return sum(numbers)


print("*args:", total(1, 2, 3, 4))


# 5. **kwargs collects extra keyword arguments into a dictionary.
def make_profile(name, **details):
	profile = {"name": name}
	profile.update(details)
	return profile


print("**kwargs:", make_profile("Sam", city="Oslo", active=True))


# 6. * expands a sequence into positional arguments.
def multiply(first, second, third):
	return first * second * third


values = (2, 3, 4)
print("Unpacked positional:", multiply(*values))


# ** expands a dictionary into keyword arguments.
def show_settings(theme, notifications):
	return f"theme={theme}, notifications={notifications}"


options = {"theme": "dark", "notifications": True}
print("Unpacked keywords:", show_settings(**options))


# 7. / makes a parameter positional-only.
#    * makes the parameters after it keyword-only.
def request(method, /, url, timeout=5, *, retries=2):
	return {
		"method": method,
		"url": url,
		"timeout": timeout,
		"retries": retries,
	}


print("Parameter kinds:", request("GET", "/items", retries=1))


# 8. Reassigning a parameter does not replace the caller's list.
def reassign_list(numbers):
	numbers = [99]
	print("inside function:", numbers)


# Changing a list does affect the shared list.
def add_number(numbers):
	numbers.append(99)


numbers = [1, 2]
reassign_list(numbers)
print("After reassignment:", numbers)
add_number(numbers)
print("After changing the list:", numbers)


# 9. A function can be passed as an argument.
def apply_to_all(numbers, operation):
	results = []
	for number in numbers:
		results.append(operation(number))
	return results


def square(number):
	return number * number


print("Callback:", apply_to_all([1, 2, 3], lambda number: square(number)))


# 10. Type hints describe expected values, but Python does not enforce them.
def safe_divide(numerator: float, denominator: float) -> float:
	if denominator == 0:
		raise ValueError("denominator must not be zero")

	return numerator / denominator


print("Division:", safe_divide(10, 4))


"""QUICK REVIEW
==============
1. What is the difference between a parameter and an argument?
   A parameter is named in a function definition. An argument is passed in a
   function call.

2. What do *args and **kwargs contain?
   *args is a tuple of extra positional arguments.
   **kwargs is a dictionary of extra keyword arguments.

3. Why should you avoid a list as a default value?
   The same list would be reused by later calls. Use None and make a new list
   inside the function instead.

4. What do / and * mean in a function definition?
   Parameters before / are positional-only. Parameters after * are
   keyword-only.

5. Can a function change a list passed to it?
   Reassigning the parameter does not replace the caller's list. Changing the
   list itself, such as with append(), is visible to the caller.

6. What happens when required arguments are missing or passed incorrectly?
   Python raises a TypeError.

7. Do type hints validate arguments?
   No. They describe expected types for readers and tools. Check values in the
   function when runtime validation is needed.
"""
