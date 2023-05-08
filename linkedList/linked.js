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
}
