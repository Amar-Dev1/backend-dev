# 📌 Lists and Sets in Different Programming Languages

## 🔍 Overview
Lists and sets are built-in data structures available in many programming languages. While they share some similarities, they have fundamental differences in how they store and manage data.

## 🛠 Mutability
**Mutability** refers to whether an object can be changed after creation:
- **Mutable objects**: Can be modified after being created.
- **Immutable objects**: Cannot be modified after being created.

### 🔷 Sets and Mutability
- **Python**: Only immutable objects can be stored in sets.
- **JavaScript**: Allows mutable objects in sets, but modification requires careful handling.
- **Kotlin**: Has immutable sets and **MutableSet** for altering elements.

## ⚡ Why Are Sets Fast?
Sets use **hashing** to store elements efficiently:
- Each element is **hashed** (converted to a unique identifier).
- The hash is used to determine its position in memory.
- This makes lookup operations **extremely fast** compared to lists.

💡 **Limitation:** If a stored element is modified, its hash changes, making it untraceable. This is why Python only allows immutable objects in sets.

## 📜 Lists
- **Ordered**: Elements maintain their insertion order.
- **Indexing**: Elements can be accessed using their position.
- **Allows Duplicates**: Unlike sets, lists can store multiple occurrences of the same value.
- **Supports Different Data Types**: Lists can store both mutable and immutable objects.

### ⏳ Lists vs. Sets Performance
- **Lists**: Searching requires checking each element sequentially → **Slower** ❌
- **Sets**: Use hashing for direct lookups → **Faster** ✅

## 🏆 When to Use What?
| Feature        | List 📝 | Set 🔢 |
|--------------|--------|--------|
| Ordered      | ✅     | ❌     |
| Allows Duplicates | ✅ | ❌ |
| Fast Lookups | ❌ | ✅ |
| Stores Mutable Objects | ✅ | ❌ (Python) / ✅ (JavaScript) |

### 🎯 Choosing the Right Data Structure
- **Use lists** when order matters or duplicates are required.
- **Use sets** when you need fast lookups and unique values.

🚀 Understanding these differences helps in selecting the right data structure for optimal performance! 🔥
