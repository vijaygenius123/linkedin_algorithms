"""
Author: Vijayaraghavan Sundararaman
Date: 02/Nov/2019
Description: Program to implement a linked list
"""

"""
 
      ___       __        _______   ______   .______       __  .___________. __    __  .___  ___. 
     /   \     |  |      /  _____| /  __  \  |   _  \     |  | |           ||  |  |  | |   \/   | 
    /  ^  \    |  |     |  |  __  |  |  |  | |  |_)  |    |  | `---|  |----`|  |__|  | |  \  /  | 
   /  /_\  \   |  |     |  | |_ | |  |  |  | |      /     |  |     |  |     |   __   | |  |\/|  | 
  /  _____  \  |  `----.|  |__| | |  `--'  | |  |\  \----.|  |     |  |     |  |  |  | |  |  |  | 
 /__/     \__\ |_______| \______|  \______/  | _| `._____||__|     |__|     |__|  |__| |__|  |__| 

    1. Insert Item To LinkedList

        a. Create A Node 
        b. Set The Next Node For New Node As The Current Head Of Linked List
        c. Set The Head As The New Node
        d. Increment Count By 1

    2. Find First Occurrence Of An Item In Linked List
        
    3. Delete An Item From Index                                                                                          
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
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while(item != None):
            if(item.get_data() == val):
                return item
            else:
                item = item.get_next()

        return None

    def deleteAt(self, idx):
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            temp_index = 0
            node = self.head
            while temp_index < idx - 1:
                node = node.get_next()
                temp_index += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while(tempnode != None):
            print("Node: {0}".format(tempnode.get_data()))
            tempnode = tempnode.get_next()


if __name__ == '__main__':
    print("Starting LinkedList")
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    print("Node Found {0}".format(ll.find(2)))
    ll.dump_list()
