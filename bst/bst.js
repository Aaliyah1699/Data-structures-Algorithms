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
      node.data = minRight.data;

      // Delete inorder successor
      node.right = this.deleteHelper(node.right, minRight.data);
    }
    return node;
  }

  // find min
  findMin(node) {
    // Helper function to find the minimum value in a subtree
    while (node.left) {
      node = node.left;
    }
    return node.data;
  }

  // find node of given value
  find(value) {
    // Call recursive function to find value
    return this.findHelper(this.root, value);
  }

  findHelper(node, value) {
    // Base case
    if (!node || node.data === value) {
      return node;
    }
    // If value is smaller than node, search in the left subtree
    if (value < node.data) {
      return this.findHelper(node.left, value);
    }

    return this.findHelper(node.right, value);
  }

  // level order traversal
  levelOrder(func = null, printLevel = false) {
    // Check if func is provided
    if (func === null) {
      const values = [];
      let levels = printLevel ? [] : null;

      // Helper to visit node and append value and level to list
      const visit = (node, level) => {
        values.push(node.data);
        if (printLevel) {
          levels.push(level);
        }
      };

      // Call level order helper with visit function
      this.levelOrderTraversal(this.root, visit);

      if (printLevel) {
        return [values, levels];
      }
      return values;
    } else {
      // Call level order helper with the provided function
      this.levelOrderTraversal(this.root, func);
    }
  }

  levelOrderTraversal(node, visit) {
    // Base case
    if (node === null) {
      return;
    }

    // Create queue and enqueue root node
    const queue = [node];

    // Loop until the queue is empty
    while (queue.length > 0) {
      // Dequeue front node
      const currentNode = queue.shift();

      // Visit current node
      visit(currentNode);

      // Enqueue left child
      if (currentNode.left !== null) {
        queue.push(currentNode.left);
      }

      // Enqueue right child
      if (currentNode.right !== null) {
        queue.push(currentNode.right);
      }
    }
  }
  // Depth first traversal
  inorder(func = null) {
    // Call the recursive function to traverse the tree
    return this.inorderHelper(this.root, func);
  }

  inorderHelper(node, func) {
    // Base case
    if (!node) {
      return [];
    }

    // Recursively traverse left subtree
    const left = this.inorderHelper(node.left, func);

    // Call function on node data
    if (func !== null) {
      func(node);
    }

    // Recursively traverse right subtree
    const right = this.inorderHelper(node.right, func);

    return left.concat([node.data], right);
  }

  preorder(func = null) {
    // Call the recursive function to traverse the tree
    return this.preorderHelper(this.root, func);
  }

  preorderHelper(node, func) {
    // Base case
    if (!node) {
      return [];
    }

    // Call function on node data
    if (func !== null) {
      func(node);
    }

    // Recursively traverse left subtree
    const left = this.preorderHelper(node.left, func);

    // Recursively traverse right subtree
    const right = this.preorderHelper(node.right, func);

    return [node.data].concat(left, right);
  }

  postorder(func = null) {
    // Call the recursive function to traverse the tree
    return this.postorderHelper(this.root, func);
  }

  postorderHelper(node, func) {
    // Base case
    if (!node) {
      return [];
    }

    // Recursively traverse left subtree
    const left = this.postorderHelper(node.left, func);

    // Recursively traverse right subtree
    const right = this.postorderHelper(node.right, func);

    // Call function on node data
    if (func !== null) {
      func(node);
    }

    return left.concat(right, [node.data]);
  }
  // height of tree
  height(node = null) {
    // Check if the tree is empty
    if (this.root === null) {
      return -1;
    }

    // Create a queue to perform level order traversal
    const queue = [[this.root, 0]];
    let maxHeight = 0;

    while (queue.length > 0) {
      const [node, level] = queue.shift();

      // Update max height
      maxHeight = Math.max(maxHeight, level);

      // Enqueue left child
      if (node.left) {
        queue.push([node.left, level + 1]);
      }

      // Enqueue right child
      if (node.right) {
        queue.push([node.right, level + 1]);
      }
    }

    return maxHeight;
  }

  depth(node) {
    // Base case
    if (node === null) {
      return -1;
    }

    // Recursively calculate the depth of the parent of the node
    const parentDepth = this.depth(node.parent);

    // Return the depth of the node
    return parentDepth + 1;
  }

  isBalanced() {
    // Return true if the tree is balanced
    return this.isBalancedHelper(this.root);
  }

  isBalancedHelper(node) {
    // Base case
    if (node === null) {
      return true;
    }

    // Calculate the height of the left and right subtrees
    const leftHeight = this.height(node.left);
    const rightHeight = this.height(node.right);

    // Check if the difference in height is greater than 1
    if (Math.abs(leftHeight - rightHeight) > 1) {
      return false;
    }

    // Recursively check if the left and right subtrees are balanced
    return (
      this.isBalancedHelper(node.left) && this.isBalancedHelper(node.right)
    );
  }

  rebalance() {
    // Get a sorted list of values in the tree
    const values = this.inorder();

    // Rebuild the tree
    this.root = this.buildTree(values);
  }
}

// Function to generate an array of random numbers
function generateRandomArray(size) {
  const array = [];
  for (let i = 0; i < size; i++) {
    array.push(Math.floor(Math.random() * 100) + 1);
  }
  return array;
}

// Driver script
function main() {
  // Create a binary search tree from an array of random numbers
  const randomArray = generateRandomArray(10);
  const tree = new Tree(randomArray);

  // Confirm that the tree is balanced
  console.log("Is the tree balanced?", tree.isBalanced());

  // Print elements in level order
  console.log("Level order traversal:");
  tree.levelOrder((node) => console.log(node.data), true);

  // Print elements in preorder
  console.log("Preorder traversal:");
  tree.preorder((node) => console.log(node.data));

  // Print elements in postorder
  console.log("Postorder traversal:");
  tree.postorder((node) => console.log(node.data));

  // Print elements in inorder
  console.log("Inorder traversal:");
  tree.inorder((node) => console.log(node.data));

  // Unbalance the tree by adding numbers > 100
  const unbalanceValues = [101, 110, 120];
  for (const value of unbalanceValues) {
    tree.insert(value);
  }

  // Confirm that the tree is unbalanced
  console.log("Is the tree unbalanced?", tree.isBalanced());

  // Balance the tree by calling rebalance
  tree.rebalance();

  // Confirm that the tree is balanced
  console.log("Is the tree balanced after rebalancing?", tree.isBalanced());

  // Print elements in level order
  console.log("Level order traversal after rebalancing:");
  tree.levelOrder((node) => console.log(node.data), true);

  // Print elements in preorder
  console.log("Preorder traversal after rebalancing:");
  tree.preorder((node) => console.log(node.data));

  // Print elements in postorder
  console.log("Postorder traversal after rebalancing:");
  tree.postorder((node) => console.log(node.data));

  // Print elements in inorder
  console.log("Inorder traversal after rebalancing:");
  tree.inorder((node) => console.log(node.data));
}

// Run the driver script
main();
