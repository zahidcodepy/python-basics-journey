# 🔹 DEFINING STRINGS
# A string is text written inside single or double quotes

a = 'Hello'     # using single quotes
b = "World"     # using double quotes

print(a)
print(b)


# 🔹 HANDLING QUOTES WITHIN STRINGS
# If you want quotes inside a string:

text1 = "He said 'Hello'"     # using different quotes (best way)
text2 = 'He said \'Hello\''  # using escape character \

print(text1)
print(text2)


# 🔹 MULTI-LINE STRINGS
# Use triple quotes for writing strings in multiple lines

multi1 = '''This is
a multi-line
string'''

multi2 = """This is
another multi-line
string"""

print(multi1)
print(multi2)


# 🔹 INDEXING + INDEX ERROR
# Indexing starts from 0

text = "Python"

print(text[0])   # P (first character)
print(text[1])   # y (second character)
print(text[-1])  # n (last character)

# If index is out of range, Python gives IndexError
# print(text[10])   ❌ Uncommenting this will cause error
