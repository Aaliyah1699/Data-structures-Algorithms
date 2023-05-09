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
}
