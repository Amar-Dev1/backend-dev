# 🌳 Understanding Trees in Programming Languages

## 🔍 What is a Tree?
A **tree** is an **abstract data type (ADT)** that organizes data in a hierarchical structure. It consists of:
- **Nodes** (individual elements)
- **Root Node** (topmost node from which all other nodes descend)
- **Leaf Nodes** (nodes with no children)

## 🌲 Binary Tree Basics
The **binary tree** is a common type of tree with the following rules:
- Each node has a **maximum of two child nodes**.
- Each node has a **key** for identification. and reference to the left and right nodes (so that the tree can be traversed). **go to (*)**
- **Smaller values** go to the **left child**, while **greater values** go to the **right child**.

### 💡 (*) This can be achieved by creating a class with these three attributes (key, location of left node, location of right node). This class will need three additional methods so that it can function as a tree. These include: 

## 🛠️ Implementing a Tree
To create a tree:
1. Define a **root node**.
2. Establish connections between nodes.
3. Each node must reference its **left** and **right** child nodes.

### 🚀 Essential Tree Operations
1. **Lookup** 🔍 - Searches for a node in the tree.
2. **Insertion** ➕ - Adds a node in the correct position.
3. **Removal** ❌ - Deletes a node while maintaining the tree structure.

## 🔎 Searching in Trees
Two main ways to search a tree:
1. **Breadth-First Search (BFS) 📏** - Explores all nodes at the current level before moving deeper.
2. **Depth-First Search (DFS) 📌** - Goes down one branch before exploring adjacent branches.

## 🔥 Key Takeaways
- Trees organize data **hierarchically**.
- Binary trees are simple and commonly used.
- Operations like lookup, insertion, and removal are essential.
- Searching can be done **horizontally (BFS)** or **vertically (DFS)**.

Understanding trees helps in **efficient data management** across different programming languages! 🚀
