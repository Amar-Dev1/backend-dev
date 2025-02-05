# 📌 Stacks & Queues

## 🏗️ What Are Stacks and Queues?
Stacks and queues are fundamental **linear data structures** used for storing and managing data with specific order rules.

- **Stack**: Follows **LIFO (Last In, First Out)**
- **Queue**: Follows **FIFO (First In, First Out)**

---

## 📦 Stack (LIFO - Last In, First Out)
A **stack** is a collection of elements where **the last added element is the first to be removed**.

### ✅ Common Stack Methods:
- `push(item)`: Adds an item to the **top**.
- `pop()`: Removes and returns the **top** item.
- `peek()/top()`: Returns the **top** item **without removing** it.
- `isEmpty()`: Checks if the stack is **empty**.
- `size()`: Returns the **number of elements** in the stack.

### 🌍 Real-World Examples:
- **Browser History**: Pressing 'Back' loads the last visited page.
- **Undo/Redo**: In text editors, actions are pushed onto a stack.
- **Call Stack in Programming**: Function calls follow LIFO.

### 🐍 Stack Implementation in Python:
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # Output: 2
```

### 🌐 Stack Implementation in JavaScript:
```javascript
class Stack {
    constructor() {
        this.stack = [];
    }
    push(item) {
        this.stack.push(item);
    }
    pop() {
        return this.stack.length ? this.stack.pop() : null;
    }
    peek() {
        return this.stack.length ? this.stack[this.stack.length - 1] : null;
    }
    isEmpty() {
        return this.stack.length === 0;
    }
    size() {
        return this.stack.length;
    }
}

// Example usage
const s = new Stack();
s.push(1);
s.push(2);
console.log(s.pop());  // Output: 2
```

---

## 🚋 Queue (FIFO - First In, First Out)
A **queue** is a collection of elements where **the first added element is the first to be removed**.

### ✅ Common Queue Methods:
- `enqueue(item)`: Adds an item to the **end**.
- `dequeue()`: Removes and returns the **front** item.
- `front()`: Returns the **front** item **without removing** it.
- `isEmpty()`: Checks if the queue is **empty**.
- `size()`: Returns the **number of elements** in the queue.

### 🌍 Real-World Examples:
- **Waiting Lines**: People in a queue at a store.
- **Task Scheduling**: Printer job queue, CPU task scheduling.
- **Message Queues**: Email and notification systems process requests in order.

### 🐍 Queue Implementation in Python:
```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if not self.is_empty() else None

    def front(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
```

### 🌐 Queue Implementation in JavaScript:
```javascript
class Queue {
    constructor() {
        this.queue = [];
    }
    enqueue(item) {
        this.queue.push(item);
    }
    dequeue() {
        return this.queue.length ? this.queue.shift() : null;
    }
    front() {
        return this.queue.length ? this.queue[0] : null;
    }
    isEmpty() {
        return this.queue.length === 0;
    }
    size() {
        return this.queue.length;
    }
}

// Example usage
const q = new Queue();
q.enqueue(1);
q.enqueue(2);
console.log(q.dequeue());  // Output: 1
```

---

## 🎯 Key Differences Between Stack & Queue
| Feature      | Stack (LIFO) | Queue (FIFO) |
|-------------|-------------|--------------|
| Order       | Last In, First Out | First In, First Out |
| Main Methods | `push()`, `pop()` | `enqueue()`, `dequeue()` |
| Real-World Use Cases | Undo history, function calls | Task scheduling, customer service |

---

## 🔥 Conclusion
- **Stacks** are useful when the last added element needs to be processed first (e.g., call stack, undo functionality).
- **Queues** are useful when elements need to be processed in the order they were added (e.g., task scheduling, customer queues).

By understanding stacks and queues, you can **efficiently manage data** in various applications! 🚀
