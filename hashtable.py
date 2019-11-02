"""
Author: Vijayaraghavan Sundararaman
Date : 2/Nov/2019
Desc : Program to experiment with hashtable
"""

# Create A Hashtable
items = dict({"key1": 1, "key2": 2, "key3": 3})

# Print the hashtable
print(items)

# Create hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3

print(items2)

# Try accessing non existant key
# print(items2['key4'])

for key, value in items2.items():
    print("Key:{0} Value{1}".format(key, value))
