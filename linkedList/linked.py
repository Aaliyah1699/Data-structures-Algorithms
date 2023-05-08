# Node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            self.tail = self.tail.next_node
        self.size += 1

    # Add node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1

    # Size of the list
    def size(self):
        return self.size
    
    # Return first node of list