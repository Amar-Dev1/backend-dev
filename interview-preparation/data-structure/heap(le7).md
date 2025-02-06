# Heap 🌳

## What is a Heap? 🤔

A **Heap** is a special tree-based data structure that satisfies the **heap property**. It is a **complete binary tree**, which means every level of the tree is fully filled except possibly the last level, and the last level is filled from left to right.

A heap can be of two types:

1. **Max Heap**: The value of each node is greater than or equal to the values of its children.
2. **Min Heap**: The value of each node is less than or equal to the values of its children.

### Key Properties 🔑
- **Heap property**: For Max Heap, each parent node’s value is greater than or equal to the values of its children. For Min Heap, each parent node’s value is less than or equal to the values of its children.
- **Complete Binary Tree**: All levels, except possibly the last, are completely filled.

---

## Why Use a Heap? 🚀

Heaps are primarily used in situations where we need to efficiently access the **maximum** or **minimum** value in a collection of elements. This makes them useful for various real-world applications:

1. **Priority Queue**: Heaps are ideal for implementing priority queues where elements with higher priority (or lower, depending on Min/Max heap) need to be processed first.
2. **Heap Sort**: Heaps can be used to sort elements in `O(n log n)` time.
3. **Dynamic Median Finding**: By maintaining a Max Heap for the smaller half of the elements and a Min Heap for the larger half, we can find the median in O(log n) time.
4. **Efficient Scheduling**: For managing resources like CPU or memory in a system, where tasks with higher priority are executed first.

---

## How Does a Heap Work? 🔄

A heap is a **binary tree**, meaning each node has at most two children. The two main operations on a heap are:

### 1. **Insert** Operation 🛠️

- When inserting a new element, we add it at the **next available spot** in the last level to maintain the complete binary tree property.
- Then, we perform a **heapify-up** operation, where the element is compared with its parent. If it violates the heap property, we swap it with its parent. This continues until the heap property is restored.

### 2. **Extract** Operation 🏗️

- The **extract** operation removes the root (the maximum value for Max Heap or minimum value for Min Heap).
- We replace the root with the last element in the tree.
- Then, we perform a **heapify-down** operation, where the root is compared with its children, and we swap it with the larger (Max Heap) or smaller (Min Heap) child. This continues until the heap property is restored.

---

## Real-World Example: **Priority Queue** 🎯

A priority queue is a data structure that stores elements in order of their priority. A **Heap** is perfect for implementing a priority queue because it allows us to:

- Insert an element in **O(log n)** time.
- Extract the highest (or lowest) priority element in **O(log n)** time.

### Example: Task Scheduling 🗓️

Imagine you have a task scheduler in an operating system. Each task has a **priority** value. The scheduler needs to always pick the task with the **highest priority** to run next.

We can use a **Max Heap** to efficiently manage the tasks:

- Insert a new task with a given priority.
- Extract the task with the highest priority.

### Python Code Example (Max Heap):

```python
import heapq

# A list to represent the heap (Priority Queue)
tasks = []

# Adding tasks with priority (negative because heapq implements Min Heap by default)
heapq.heappush(tasks, (-5, 'Task 1'))  # Task 1 has priority 5
heapq.heappush(tasks, (-2, 'Task 2'))  # Task 2 has priority 2
heapq.heappush(tasks, (-3, 'Task 3'))  # Task 3 has priority 3

# Extracting tasks in order of priority
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Executing: {task} with priority {-priority}")

# Output:    
Executing: Task 1 with priority 5
Executing: Task 3 with priority 3
Executing: Task 2 with priority 2
```
## When to Use a Heap? 🧠
- You need efficient access to the maximum or minimum element.
- You need a priority queue where elements need to be processed based on priority.
- You need to implement algorithms that require heap sorting or median finding.