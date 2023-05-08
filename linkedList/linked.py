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
    def head(self):
        return self.head
    
    # Return last node of list
    def tail(self):
        return self.tail
    
    # Return node at index
    def at(self, index):
        if index < 0 or index >= self.size:
            return None
        current_node = self.head
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
        return current_node
            
    # Remove node at index
    def remove(self, index):
        if self.head is None:
            return None
        current_node = self.head
        previous_node = None
        while current_node.next_node is not None:
            previous_node = current_node
            current_node = current_node.next_node
        if previous_node is None:
            self.head = None
            self.tail = None
        else:
            previous_node.next_node = None
            self.tail = previous_node
        self.size -= 1
        return current_node.value
    
    # If value is in the list
    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False
    