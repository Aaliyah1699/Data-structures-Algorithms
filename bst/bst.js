// Class node
class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Tree class
class Tree {
  constructor(array) {
    this.root = this.buildTree([...new Set(array)].sort());
  }

  // Build tree
  buildTree(array) {
    // Base case
    if (!array.length) {
      return null;
    }

    // find middle and make it root
    const mid = Math.floor(array.length / 2);
    const root = new Node(array[mid]);

    // Recursively build left and right subtree
    root.left = this.buildTree(array.slice(0, mid));
    root.right = this.buildTree(array.slice(mid + 1));

    return root;
  }

  // insert node
  insert(value) {
    // Call recursive function to insert value
    this.root = this.insertHelper(this.root, value);
  }

  insertHelper(node, value) {
    // Base case
    if (!node) {
      return new Node(value);
    }
    // If value is less than node value, go left
    if (value < node.value) {
      node.left = this.insertHelper(node.left, value);
    }
    // If value is greater than node value, go right
    else {
      node.right = this.insertHelper(node.right, value);
    }
    return node;
  }
  // delete node
  delete(value) {
    // Call recursive function to delete value
    this.root = this.deleteHelper(this.root, value);
  }

  deleteHelper(node, value) {
    // Base case
    if (!node) {
      return node;
    }
    // If value is smaller than node delete from left subtree
    if (value < node.value) {
      node.left = this.deleteHelper(node.left, value);
    }
    // If value is greater than node delete from right subtree
    else if (value > node.value) {
      node.right = this.deleteHelper(node.right, value);
    }
    // If value is equal to node, delete node
    else {
      // If node has one or no children
      if (!node.left) {
        return node.right;
      } else if (!node.right) {
        return node.left;
      }
      // If node has two children
      // Get inorder successor
      const minRight = this.findMin(node.right);

      // Copy inorder successor's content to node
      node.value = minRight.value;

      // Delete inorder successor
      node.right = this.deleteHelper(node.right, minRight.value);
    }
    return node;
  }

  // find min
  findMin(node) {
    let current = node;
    while (current && current.left) {
      current = current.left;
    }
    return current;
  }
}
