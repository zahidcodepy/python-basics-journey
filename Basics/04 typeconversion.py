# TYPEcasting in python 
# Conversion 1 datatype to another
# typeconversion 
a = "1"
b = "2" 
print(a+b)  # output : "12" string concatenation


# Two type of type casting 

# 1. implicit(AUTOMATIC)

c = 2 # INT 
d = 3.2 # FLOAT
print(c+d) # o/p : 5.2 (INT->float automatically)

# 2. explicit(manual)

e = 1
f = 2
print(e+f) # o/p: 3

""" IMPORTANT for interview """
# boolean typecasting
bool(0) # FALSE
bool(1) # TRUE
bool("") # FALSE
bool("KHAN") # TRUE
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("KHAN"))
