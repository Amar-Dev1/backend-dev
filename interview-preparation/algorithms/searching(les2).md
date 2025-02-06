# 📌 Search Algorithms

In this section, we explore the time and space complexity of **linear search** and **binary search** to understand their efficiency in finding a target element.

---

## 🔍 Linear Search
Linear search is the simplest searching technique, iterating through the list sequentially until the target element is found or the list ends.

### ✅ **Steps**:
1. Start from the first element.
2. Compare each element with the target.
3. If a match is found, return the index.
4. If the end of the list is reached, return "Not Found."

### 📊 **Complexity Analysis**:
- **Worst Case**: The target is absent, requiring a full scan → **O(n)**
- **Average Case**: The target is in the middle → **O(n)**
- **Best Case**: The target is the first element → **O(1)**
- **Space Complexity**: No extra space required → **O(1)**

---

## 🔎 Binary Search
Binary search is an efficient searching technique that works on a **sorted list** by dividing the search space in half at each step.

### ✅ **Steps**:
1. Find the middle element.
2. If it matches the target, return the index.
3. If the target is smaller, repeat the search in the left half.
4. If the target is larger, repeat in the right half.
5. Continue until the element is found or the search space is empty.

### 📊 **Complexity Analysis**:
- **Worst Case**: The element is absent → **O(log n)**
- **Average Case**: Found after multiple iterations → **O(log n)**
- **Best Case**: Found at the first check → **O(1)**
- **Space Complexity**: No extra space required → **O(1)**

---

### 🔥 **Key Takeaways**:
- **Linear search** is simple but inefficient for large lists.
- **Binary search** is much faster but requires sorting beforehand.
- **Space complexity** remains constant at **O(1)** for both methods.

🚀 **For larger datasets, always prefer binary search if the data is sorted!**

