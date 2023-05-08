# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Tree class
class Tree:
    def __init__(self, values):
        self.root = self.build_tree(values)