# The while loop repeatedly executes a block of code as long as a given condition remainsTrue.

# SYNTAX
# while condition:
    # code block to be executed

# EXAMPLE

COUNT = 0 
while COUNT < 6:       # CONDITION
    print(COUNT)
    COUNT +=1          # INCREMENTING THE COUNT VARIABLE TO AVOID INFINITE LOOP
    
# Output:
# 0
# 1
# 2
# 3
# 4
# 5

# In this example, the while loop will continue to execute as long as the value of COUNT is less than 6.
# If we forget to increment the COUNT variable, the loop will run indefinitely, resulting in an infinite loop.
