"""
Author: Vijayaraghavan Sundararaman
Date: 02/Nov/2019
Description: Program to implement a linked list
"""


class Node(object):
    """Class representing a Node in a linked list

    """

    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # //TODO insert a new node
        new_node = Node(data)

    def find(self, val):
        // TODO find the first element with given value
        item = self.head

    def deleteAt(self, idx):
        # //TODO delete an item at give  index
        if idx > self.count-1:
            return

    def dump_list(self):
        tempnode = self.head
        while(tempnode != None):
            print("Node: {0}", tempnode.get_data)
            tempnode = tempnode.get_next()
