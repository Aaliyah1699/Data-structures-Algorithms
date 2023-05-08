# Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


# Linked List
class LinkedList:
    def __init__(self):
        self.head_node_node = None
        self.tail_node = None
        self.size = 0

    # Add node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head_node_node is None:
            self.head_node = new_node
            self.tail_node = self.head_node
        else:
            self.tail_node.next_node = new_node
            self.tail_node = self.tail_node.next_node
        self.size += 1

    # Add node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = self.head_node
        else:
            new_node.next_node = self.head_node
            self.head_node = new_node
        self.size += 1

    # Size of the list
    def get_size(self):
        return self.size

    # Return first node of list
    def head(self):
        return self.head_node

    # Return last node of list
    def tail(self):
        return self.tail_node

    # Return node at index
    def at(self, index):
        if index < 0 or index >= self.size:
            return None
        current_node = self.head_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
        return current_node

    # Remove node 
    def pop(self):
        if self.head_node is None:
            return None
        popped_value = self.tail_node.value

        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
        else:
            current_node = self.head_node
            while current_node.next_node != self.tail_node:
                current_node = current_node.next_node
            current_node.next_node = None
            self.tail_node = current_node

        self.size -= 1
        return popped_value

    # If value is in the list
    def contains(self, value):
        current_node = self.head_node
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    # find index of node containing value or null
    def find(self, value):
        current_node = self.head_node
        current_index = 0
        while current_node is not None:
            if current_node.value == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1
        return None

    # Return string representation of list
    def to_string(self):
        string = ""
        current_node = self.head_node
        while current_node is not None:
            string += str(current_node.value) + " "
            current_node = current_node.next_node
        string += "null"
        return string

    # insert at given index
    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            new_node = Node(value)
            current_node = self.head_node
            previous_node = None
            current_index = 0
            while current_index < index:
                previous_node = current_node
                current_node = current_node.next_node
                current_index += 1
            previous_node.next_node = new_node
            new_node.next_node = current_node
            self.size += 1

    # remove at given index
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head_node = self.head_node.next_node
            self.size == 1
            self.tail_node = None
        else:
            current_node = self.head_node
            previous_node = None
            current_index = 0
            while current_index < index:
                previous_node = current_node
                current_node = current_node.next_node
                current_index += 1
            previous_node.next_node = current_node.next_node
            if index == self.size - 1:
                self.tail_node = previous_node
            self.size -= 1

# Test

# Create a new LinkedList instance
list = LinkedList()

# Append nodes
list.append(10)
list.append(20)
list.append(30)

# Prepend nodes
list.prepend(5)
list.prepend(2)

# Test size, head, and tail
print("Size:", list.get_size())         # Output: 5
print("Head:", list.head().value)   # Output: 2
print("Tail:", list.tail().value)   # Output: 30

# Test at
print("Node at index 2:", list.at(2).value)   # Output: 10

# Test pop
print("Popped element:", list.pop())          # Output: 30

# Test contains
print("Contains 20:", list.contains(20))      # Output: True
print("Contains 40:", list.contains(40))      # Output: False

# Test find
print("Index of 20:", list.find(20))          # Output: 2

# Test toString
print("LinkedList:", list.toString())         # Output: (2) -> (5) -> (10) -> (20) -> null

# Test insertAt
list.insertAt(15, 2)
print("LinkedList after insertion:", list.toString())   # Output: (2) -> (5) -> (15) -> (10) -> (20) -> null

# Test removeAt
list.removeAt(3)
print("LinkedList after removal:", list.toString())     # Output: (2) -> (5) -> (15) -> (20) -> null
