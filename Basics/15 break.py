# break Statement: The break statement terminates the loop entirely, exiting from it immediately.
# It is commonly used to exit a loop when a certain condition is met, preventing further iterations.

# SYNTAX
# while condition:
    # code block to be executed
    # if some_condition:
        # break 

# EXAMPLE for break statement in a for loop
i = 0
for i in range(5):
     print(i)
     if i == 3:
        break

# output:
# 0
# 1
# 2
# 3
# In this example, the for loop iterates over the range of numbers from 0 to 4.
# When the variable 'i' reaches the value of 3, the break statement is executed, which causes the loop to terminate immediately.
# as a result, the loop will not count beyond 3.

# EXAMPLE for break statement in a while loop

count = 0 
while count < 10:
    print(count)
    if count == 5:
        break
    count = count + 1
# output:
# 0
# 1
# 2
# 3
# 4
# 5
# In this example, the while loop continues to execute as long as the value of 'count' is less than 10.
# When 'count' reaches the value of 5, the break statement is executed, which causes the loop to terminate immediately.
# As a result, the loop will not count beyond 5.
