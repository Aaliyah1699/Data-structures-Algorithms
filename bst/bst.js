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
}
