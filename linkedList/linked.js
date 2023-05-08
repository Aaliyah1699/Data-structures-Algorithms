// Node class
class Node {
  constructor(value) {
    this.value = value;
    this.nextNode = null;
  }
}

// Linked List class
class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  // Add node to the end of the list
  append(value) {
    const newNode = new Node(value);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.nextNode = newNode;
      this.tail = newNode;
    }
    this.size++;
  }

  // Add node to the beginning of the list
  prepend(value) {
    const newNode = new Node(value);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.nextNode = this.head;
      this.head = newNode;
    }
    this.size++;
  }

  // Insert node at a given index
  at(index) {
    if (index < 0 || index >= this.size) {
      return null;
    }
    let currentNode = this.head;
    let currentIndex = 0;
    while (currentIndex < index) {
      currentNode = currentNode.nextNode;
      currentIndex++;
    }
    return currentNode;
  }

  // Remove node at a given index
  pop() {
    if (this.head === null) {
      return null;
    }
    let currentNode = this.head;
    let previousNode = null;
    while (currentNode.nextNode !== null) {
      previousNode = currentNode;
      currentNode = currentNode.nextNode;
    }
    if (previousNode === null) {
      this.head = null;
      this.tail = null;
    } else {
      previousNode.nextNode = null;
      this.tail = previousNode;
    }
    this.size--;
    return currentNode.value;
  }

  // Check if value exists in the list
  contains(value) {
    let currentNode = this.head;
    while (currentNode !== null) {
      if (currentNode.value === value) {
        return true;
      }
      currentNode = currentNode.nextNode;
    }
    return false;
  }

  // find the index of a given value
  find(value) {
    let currentNode = this.head;
    let currentIndex = 0;
    while (currentNode !== null) {
      if (currentNode.value === value) {
        return currentIndex;
      }
      currentNode = currentNode.nextNode;
      currentIndex++;
    }
    return null;
  }

  // list objects as strings
  toString() {
    let result = "";
    let currentNode = this.head;
    while (currentNode !== null) {
      result += `${currentNode.value} ->`;
      currentNode = currentNode.nextNode;
    }
    result += "null";
    return result;
  }

  // insert a node at a given index
  insertAt(index, value) {
    if (index < 0 || index >= this.size) {
      return;
    }
    if (index === 0) {
      this.prepend(value);
    } else if (index === this.size) {
      this.append(value);
    } else {
      const newNode = new Node(value);
      let currentNode = this.head;
      let previousNode = null;
      let currentIndex = 0;

      while (currentIndex < index) {
        previousNode = currentNode;
        currentNode = currentNode.nextNode;
        currentIndex++;
      }
      previousNode.nextNode = newNode;
      newNode.nextNode = currentNode;
      this.size++;
    }
  }

  // remove a node at a given index
  removeAt(index) {
    if (index < 0 || index >= this.size) {
      return;
    }
    if (index === 0) {
      this.head = this.head.nextNode;
      if (this.size === 1) {
        this.tail = null;
      }
    } else {
      let currentNode = this.head;
      let previousNode = null;
      let currentIndex = 0;

      while (currentIndex < index) {
        previousNode = currentNode;
        currentNode = currentNode.nextNode;
        currentIndex++;
      }
      previousNode.nextNode = currentNode.nextNode;
      if (index === this.size - 1) {
        this.tail = previousNode;
      }
    }
    this.size--;
  }
}

// test
// Create a new LinkedList instance
const list = new LinkedList();

// Append nodes
list.append(10);
list.append(20);
list.append(30);

// Prepend nodes
list.prepend(5);
list.prepend(2);

// Test size, head, and tail
console.log("Size:", list.size); // Output: 5
console.log("Head:", list.head.value); // Output: 2
console.log("Tail:", list.tail.value); // Output: 30

// Test at
console.log("Node at index 2:", list.at(2).value); // Output: 10

// Test pop
console.log("Popped element:", list.pop()); // Output: 30

// Test contains
console.log("Contains 20:", list.contains(20)); // Output: true
console.log("Contains 40:", list.contains(40)); // Output: false

// Test find
console.log("Index of 20:", list.find(20)); // Output: 2

// Test toString
console.log("LinkedList:", list.toString()); // Output: (2) -> (5) -> (10) -> (20) -> null

// Test insertAt
list.insertAt(15, 2);
console.log("LinkedList after insertion:", list.toString()); // Output: (2) -> (5) -> (15) -> (10) -> (20) -> null

// Test removeAt
list.removeAt(3);
console.log("LinkedList after removal:", list.toString()); // Output: (2) -> (5) -> (15) -> (20) -> null
