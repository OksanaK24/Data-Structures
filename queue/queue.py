"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Arrays
# class Queue:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0)
#         else:
#             print("You can't remove anything from an empty array")

# Linked Lists
class Node:
    def __init__(self, node = None):
        self.node = node
        self.next_node = None

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_item = Node(value)
        if self.size == 0:
            self.head = new_item
            self.head.next_node = new_item
            self.tail = new_item
        else:
            self.tail.next_node = new_item
            self.tail = new_item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("You can't remove anything from an empty array")
        elif self.size == 1:
            data_to_remove = self.head.node
            self.head.node = None
            self.tail.node = None
            self.size -= 1
            return data_to_remove
        else:
            data_to_remove = self.head.node
            self.head = self.head.next_node
            self.size -= 1
            return data_to_remove