"""
Author: Vijayaraghavan Sundararaman
Date : 2/Nov/2019
Desc : Program to experiment with queue
"""
from collections import deque

# Create a empty queue
queue = deque()

# Add items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the queue
print(queue)

# Pop an item off the front of the queue
x = queue.popleft()
print("Popped {0}".format(x))

# Print the queue
print(queue)
