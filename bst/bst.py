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

    def build_tree(self, values):
        # Use recursion to build the tree
        def build_node(arr, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = Node(arr[mid])
            node.left = build_node(arr, start, mid - 1)
            node.right = build_node(arr, mid + 1, end)
            return node
        
        # Sort the array
        values.sort()

        # Call the recursive function
        return build_node(values, 0, len(values) - 1)
