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
            if node is None or node.data == value:
                return node
            # If value is smaller than node, search in left subtree
            if value < node.data:
                return self.find_helper(node.left, value)

            return self.find_helper(node.right, value)

            
        def inorder(self, func=None):
            # Call the recursive function to traverse the tree
            return self.inorder_helper(self.root, func)
        
        def inorder_helper(self, node, func):
            # Base case
            if not node:
                return []

            # Recursively traverse left subtree
            left =  self.inorder_helper(node.left, func)

            # Call function on node data
            if func is not None:
                    func(node)

            # Recursively traverse right subtree
            right = self.inorder_helper(node.right, func)

            return left + [node.data] + right

        def preorder(self, func=None):
            # Call the recursive function to traverse the tree
            return self.preorder_helper(self.root, func)
        
        def preorder_helper(self, node, func):
            # Base case
            if not node:
                return []

            # Call function on node data
            if func is not None:
                    func(node)

            # Recursively traverse left subtree
            left =  self.preorder_helper(node.left, func)

            # Recursively traverse right subtree
            right = self.preorder_helper(node.right, func)

            return [node.data] + left + right
        
        def postorder(self, func=None):
            # Call the recursive function to traverse the tree
            return self.postorder_helper(self.root, func)
        
        def postorder_helper(self, node, func):
            # Base case
            if not node:
                return []

            # Recursively traverse left subtree
            left =  self.postorder_helper(node.left, func)

            # Recursively traverse right subtree
            right = self.postorder_helper(node.right, func)

            # Call function on node data
            if func is not None:
                    func(node)

            return left + right + [node.data]
        
        def height(self, node=None):
           # If node isn't specified, use root
            if node is None:
                node = self.root

            # Base case
            if node is None:
                return -1
            
            # Recursively calculate height of left and right subtrees
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            # Return max height of subtree l & r
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            # Return max height of subtree l & r
            return max(left_height, right_height) + 1
        
        def depth(self, node):
            # Base case
            if node is None:
                return -1

            # Recursively calculate depth of parent of node
            parent_depth = self.depth(node.parent)

            # Return depth of node
            return parent_depth + 1
        
        def is_balanced(self):
            # Return True if tree is balanced
            return self.is_balanced_helper(self.root)
        
        def is_balanced_helper(self, node):
            # Base case
            if node is None:
                return True

            # Calculate height of left and right subtrees
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            # Check if difference in height i greater than 1
            if abs(left_height - right_height) > 1:
                return False
            
            # Recursively check if left and right subtrees are balanced
            return self.is_balanced_helper(node.left) and self.is_balanced_helper(node.right)
        
        def rebalance(self):
            # Get sorted list of values in tree
            values = self.inorder()

            # Rebuild tree
            self.root = self.build_tree(values)

