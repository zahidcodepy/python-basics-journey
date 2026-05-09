# IF ELSE STATEMENT
# Used for decision making
# EXAMPLE
age = 18
if age >= 18:
    print("You can vote")
else:
    print("You can not vote")

# IF ELIF ELSE STATEMENT
# USED WHEN MULTIPLE CONDITION EXIST
# EXAMPLE
MARKS = 88
if MARKS>=90:
    print("Excellent")  
elif MARKS>=70:
    print("Good") 
elif MARKS>=50:
    print("Average")      
else:
    print("Fail")

# Nested If Statement
# we can use if,if-else,elif statement inside other if statement as well
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")


# Practice Problem 
num = int(input("Enter number: ")) 

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
