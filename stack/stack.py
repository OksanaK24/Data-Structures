"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Arrays
# class Stack:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()
#         else:
#             print("You can't remove anything from an empty array")


# Linked Lists
class Node:
    def __init__(self, node = None):
        self.node = node
        self.next_node = None

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def push(self, value):
        new_item = Node(value)
        if self.size == 0:
            self.head = new_item
            self.head.next_node = new_item
            self.tail = new_item
        else:
            self.tail.next_node = new_item
            self.tail = new_item
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("You can't remove anything from an empty array")
        elif self.size == 1:
            data_to_remove = self.tail.node
            self.head.node = None
            self.tail.node = None
            self.size -= 1
            return data_to_remove
        else:
            second_last = self.head 
            while(second_last.next_node.next_node): 
                second_last = second_last.next_node
            data_to_remove = second_last.next_node.node
            self.tail = second_last
            second_last.next_node = None
            self.size -= 1
            return data_to_remove 