"""
Author: Vijayaraghavan Sundararaman
Date : 2/Nov/2019
Desc : Program to experiment with stack
"""

# Create a stack
stack = []

# Push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# Print the stack
print(stack)

# Pop item from stack
x = stack.pop()
print("Popped {0}".format(x))

# Print the stack
print(stack)
