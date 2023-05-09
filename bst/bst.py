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
        
        def delete(self, value):
            # Call the recursive function to delete the value
            self.root = self.delete_helper(self.root, value)

        def delete_helper(self, node, value):
            # Base case
            if not node:
                return node

            # If value is smaller than node, delete from left subtree
            if value < node.data:
                node.left = self.delete_helper(node.left, value)

            # If value is greater than node, delete from right subtree
            elif value > node.data:
                node.right = self.delete_helper(node.right, value)

            # If value is same as node, delete the node
            else:
                # If node has one or no children
                if node.left is None:
                    return node.right
            
                elif node.right is None:
                    return node.left

                # If node has two children
                # Get in order successor
                min_right = self.get_min_value_node(node.right)

                # Copy in order successor's content to node
                node.data = min_right.data

                # Delete in order successor
                node.right = self.delete_helper(node.right, min_right.data)

            return node
        
        def find_min(self, node):
            # Helper function to find minimum value in subtree
            while node.left:
                node = node.left
            return node.data
        
        def find(self, value):
            # Call the recursive function to find the value
            return self.find_helper(self.root, value)
        
        def find_helper(self, node, value):
            # Base case
            if not node:
                return None

            # If value is smaller than node, search in left subtree
            if value < node.data:
                return self.find_helper(node.left, value)

            # If value is greater than node, search in right subtree
            elif value > node.data:
                return self.find_helper(node.right, value)

            # If value is same as node, return node
            else:
                return node