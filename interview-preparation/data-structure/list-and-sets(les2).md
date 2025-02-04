# 📋 Lists and Sets

## 📌 Lists
- An abstract concept referring to a container of elements.
- Can be implemented using either **arrays** or **linked lists**.
- In most programming languages, lists are represented as objects.
- Have built-in methods for **searching, sorting, and more**.

### 📌 Array-Based List
- Some languages require an **initial size**, while others adjust automatically.
- In dynamic languages, when the array reaches its **initial size**, a new larger copy is created.

### 🔗 Linked List
- A collection of **nodes**, where each node stores **data** and a **pointer** to the next node.
- Types of linked lists:
  - **Singly Linked List** → Each node points to the next node.
  - **Doubly Linked List** → Each node points to both the next and previous nodes.
  - **Circular Linked List** → The last node links back to the first node.
- Used when frequent **insertions and deletions** are needed.

---

## 🔥 Sets
- A collection of **unique elements** (no duplicates).
- Use **hashing functions** for quick lookup operations.
- Common operations:
  - **Union (A ∪ B)** → Combines two sets.
  - **Intersection (A ∩ B)** → Finds common elements.
  - **Difference (A - B)** → Elements in A but not in B.
  - **Subset (A ⊆ B)** → Checks if A is contained in B.
- Fast operations compared to lists for **membership checks**.
