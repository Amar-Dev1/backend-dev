# 🔥 Understanding Hash Tables

## 🔑 What is a Hash Table?
A **hash table** is a data structure that stores **key-value pairs** and provides **fast lookups** 🚀. This is achieved through a **hashing function**, which converts an input into a unique identifier (hash) used for storing and retrieving data efficiently.

### 🏆 Benefits of Hash Tables
- ✅ **Fast lookup** Direct access using keys instead of searching through a list.
- ✅ **Efficient memory usage** Values are stored in an optimal location.
- ✅ **Ideal for large datasets** Reduces time complexity compared to linear searches.

---

## 🛠️ Implementing Hash Tables
Many programming languages **do not** provide built-in hash table implementations but offer alternative structures that function similarly.

### 📝 Hash Tables in Kotlin
- Kotlin does not have a native hash table.
- **Alternative:** Uses **HashMap** 🗂️, which is similar but **not thread-safe**.
- **Key Differences:**
  - Allows `null` keys and values ❌
  - Requires additional code for synchronization to be thread-safe.

#### 💡 Thread Safety in Hash Tables
🖥️ **Thread-safe** means multiple threads can access and modify the structure **without errors**.
- If five different processes are modifying a hash table, the data must remain consistent.
- **HashMaps in Kotlin are not thread-safe**, so synchronization techniques must be implemented manually.

---

### 🐍 Hash Tables in Python
- Python **does not** have a built-in hash table.
- **Alternative:** Uses **dictionaries (`dict`)**, which function like a hash table.
- **Advantages of `dict` over HashMap:**
  - **Thread-safe by default** ✅
  - **Faster** due to optimized memory allocation.
  - **Supports hashing for quick lookups** 🔍

#### 🔧 Example: Python Dictionary as a Hash Table
```python
# Creating a simple hash table using a dictionary
data = {}
data['name'] = 'Alice'
data['age'] = 25

# Fast lookup
print(data['name'])  # Output: Alice
```

---


### Hash Table with Collision Handling 💥
Sometimes, two different keys might hash to the same index (collision). We need a way to handle this.

Let’s see an example with a **hash function** that only returns values between **0 and 3** (just for simplicity).

### Simple Example:

- **Keys**: "cat", "dog", "bat", "rat"
- **Hash function**: Takes the first letter of each key and calculates `ord(letter) % 4`.

Let's calculate the hash for each key:

| Key | First Letter | Hash Value (`ord(letter) % 4`) |
| --- | ------------  | ----------------------------- |
| "cat" | 'c' | `ord('c') % 4 = 99 % 4 = 3` |
| "dog" | 'd' | `ord('d') % 4 = 100 % 4 = 0` |
| "bat" | 'b' | `ord('b') % 4 = 98 % 4 = 2` |
| "rat" | 'r' | `ord('r') % 4 = 114 % 4 = 2` |

Now, let’s place the values in the hash table (size 4).

### Initial Hash Table:

| Index | Value |
| ----- | ----- |
| 0     | dog   |
| 1     |       |
| 2     | bat, rat (collision) |
| 3     | cat   |

### Collision Handling ⚔️

For the keys "bat" and "rat", both have the same hash value (2), so they are stored at index 2. But we can handle this using **chaining** (linked lists) or **open addressing**.

### Chaining Solution 🔗

In chaining, if two keys hash to the same index, we store them as a list at that index.

### Hash Table with Chaining:

| Index | Value          |
| ----- | -------------- |
| 0     | dog            |
| 1     |                |
| 2     | bat → rat      |
| 3     | cat            |

Now, **bat** and **rat** are linked together at index 2.

### Open Addressing Solution 🏠

In open addressing, if there's a collision, we find the next available spot. For example, if index 2 is occupied, we check index 3, then index 0, and so on.

With **open addressing**, the table might look like this:

| Index | Value          |
| ----- | -------------- |
| 0     | dog            |
| 1     |                |
| 2     | bat            |
| 3     | cat            |
| 0     | rat (replaces dog) |

---


## 🚀 Key Takeaways
- A **hash table** provides **fast lookup** using a **hashing function**.
- Kotlin uses **HashMaps** (not thread-safe), requiring manual synchronization.
- Python uses **dictionaries**, which are **thread-safe and optimized**.
- Selecting the right **hash table alternative** depends on **thread safety** and **performance needs**.
