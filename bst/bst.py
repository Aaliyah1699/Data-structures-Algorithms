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

    def build_tree(self, array):
        # Initialize tree with array and set root
        self.root = self.build_tree(sorted(set(array)))

        # Build tree
        def build_tree(self, array):
            # Base case
            if not array:
                return None

            # Find middle of array and make it root
            mid = len(array) // 2
            root = Node(array[mid])

            # Recursively build left and right subtrees
            root.left = self.build_tree(array[:mid])
            root.right = self.build_tree(array[mid + 1 :])

            return root

        def insert(self, value):
            # Call the recursive function to insert the value
            self.root = self.insert_helper(self.root, value)

        def insert_helper(self, node, value):
            # Base case
            if not node:
                return Node(value)

            # If value is smaller than node, insert in left subtree
            if value < node.data:
                node.left = self.insert_helper(node.left, value)

            # If value is greater than node, insert in right subtree
            else:
                node.right = self.insert_helper(node.right, value)

            return node