import random
import sys


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Tree class
class Tree:
    def __init__(self, array):
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

    def level_order(self, func=None):
        # Check if func is provided
        if func is None:
            values = []

            # Helper to visit node and append value to list
            def visit(node):
                values.append(node.data)

            # Call level order helper with visit function
            self.level_order_helper(self.root, visit)

            return values

        else:
            # Call level order helper with provided function
            self.level_order_helper(self.root, func)

    def level_order_traversal(self, node, visit):
        # Base case
        if node is None:
            return

        # Create queue and enqueue root node
        queue = [node]

        # Loop until queue is empty
        while len(queue) > 0:
            # Dequeue front node
            current_node = queue.pop(0)

            # Visit current  node
            visit(current_node)

            # Enqueue left child
            if current_node.left is not None:
                queue.append(current_node.left)

            # Enqueue right child
            if current_node.right is not None:
                queue.append(current_node.right)

    def inorder(self, func=None):
        # Call the recursive function to traverse the tree
        return self.inorder_helper(self.root, func)

    def inorder_helper(self, node, func):
        # Base case
        if not node:
            return []

        # Recursively traverse left subtree
        left = self.inorder_helper(node.left, func)

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
        left = self.preorder_helper(node.left, func)

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
        left = self.postorder_helper(node.left, func)

        # Recursively traverse right subtree
        right = self.postorder_helper(node.right, func)

        # Call function on node data
        if func is not None:
            func(node)

        return left + right + [node.data]

    def height(self, node=None):
        # check if tree is empty
        if self.root is None:
            return -1

        # Create queue to perform level order traversal
        queue = [(self.root, 0)]
        max_height = 0

        while queue:
            node, level = queue.pop(0)

            # Update max height
            max_height = max(max_height, level)

            # Enqueue left child
            if node.left:
                queue.append((node.left, level + 1))

            # Enqueue right child
            if node.right:
                queue.append((node.right, level + 1))

        return max_height

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
        return self.is_balanced_helper(node.left) and self.is_balanced_helper(
            node.right
        )

    def rebalance(self):
        # Get sorted list of values in tree
        values = self.inorder()

        # Rebuild tree
        self.root = self.build_tree(values)


# Function to generate an array of random numbers
def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]


# Driver script
def main():
    sys.setrecursionlimit(1000)

    # Create a binary search tree from an array of random numbers
    random_array = generate_random_array(10)
    tree = Tree(random_array)

    # Confirm that the tree is balanced
    print("Is the tree balanced?", tree.is_balanced())

    # Print elements in level order
    print("Level order traversal:")
    tree.level_order(lambda node: print(node.data), True)

    # Print elements in preorder
    print("Preorder traversal:")
    tree.preorder(lambda node: print(node.data))

    # Print elements in postorder
    print("Postorder traversal:")
    tree.postorder(lambda node: print(node.data))

    # Print elements in inorder
    print("Inorder traversal:")
    tree.inorder(lambda node: print(node.data))

    # Unbalance the tree by adding numbers > 100
    unbalance_values = [101, 110, 120]
    for value in unbalance_values:
        tree.insert(value)

    # Confirm that the tree is unbalanced
    print("Is the tree unbalanced?", tree.is_balanced())

    # Balance the tree by calling rebalance
    tree.rebalance()

    # Confirm that the tree is balanced
    print("Is the tree balanced after rebalancing?", tree.is_balanced())

    # Print elements in level order
    print("Level order traversal after rebalancing:")
    tree.level_order(lambda node: print(node.data), True)

    # Print elements in preorder
    print("Preorder traversal after rebalancing:")
    tree.preorder(lambda node: print(node.data))

    # Print elements in postorder
    print("Postorder traversal after rebalancing:")
    tree.postorder(lambda node: print(node.data))

    # Print elements in inorder
    print("Inorder traversal after rebalancing:")
    tree.inorder(lambda node: print(node.data))


# Run the driver script
if __name__ == "__main__":
    main()
