# 📌 Sorting Algorithms

Understanding time and space complexity helps in evaluating the efficiency of sorting algorithms. In this document, we will explore the time and space complexity of **Selection Sort** and **Quicksort**, two common sorting algorithms used for arrays.

---

## 🔷 Selection Sort

**Selection Sort** is a simple sorting algorithm that iterates over the array from left to right, swapping the current element with the smallest value found in the remaining part of the array.

### ⏳ Time Complexity
- **Worst Case**: **O(n²)**
- **Average Case**: **O(n²)**
- **Best Case**: **O(n²)**

### 💾 Space Complexity
- **O(1)** (In-place swap, requires no extra space apart from a few variables)

### 🛠 Steps to Perform Selection Sort
1. Find the **smallest** value and swap it with the **first** element.
2. Find the **second smallest** value and swap it with the **second** element.
3. Repeat this process until the entire array is sorted.

### 📜 Pseudocode
```cpp
for(i = 0; i < n-1; i++) {
    int min_index = i;
    for(j = i+1; j < n; j++) {
        if(List[j] < List[min_index]) {
            min_index = j;
        }
    }
    swap(List[i], List[min_index]);
}
```

### 🔎 Complexity Analysis
- **Worst case**: When the list is sorted in **reverse order**, we get **O(n²)**.
- **Average case**: Every item must be checked against all others, leading to **O(n²)**.
- **Best case**: Even for a sorted list, **O(n²)** comparisons are still made.

---

## 🔷 Quicksort

**Quicksort** is a **divide-and-conquer** algorithm that selects a pivot and partitions the array into two halves: elements smaller than the pivot go to the left, and elements greater go to the right.

### ⏳ Time Complexity
- **Worst Case**: **O(n²)** (if the worst pivot is always chosen)
- **Average Case**: **O(n log n)**
- **Best Case**: **O(n log n)** (if an optimal pivot is chosen)

### 💾 Space Complexity
- **O(n)** (recursive calls take up stack memory)
- **O(log n)** if implemented with **in-place partitioning**

### 🛠 Steps to Perform Quicksort
1. **Choose a pivot** from the list.
2. **Partition** the list into two halves:
   - Elements **smaller** than the pivot go to the **left**.
   - Elements **greater** than the pivot go to the **right**.
3. **Recursively apply** the same process to both halves until the list is sorted.

### 📜 Pseudocode
```cpp
QuickSort(List, low, high) {
    if (low < high) {
        pivot = partition(List, low, high);
        QuickSort(List, low, pivot - 1);
        QuickSort(List, pivot + 1, high);
    }
}

Partition(List, low, high) {
    pivot = List[high];
    i = (low - 1);
    for (j = low; j <= high - 1; j++) {
        if (List[j] < pivot) {
            i++;
            swap(List[i], List[j]);
        }
    }
    swap(List[i + 1], List[high]);
    return i + 1;
}
```

### 🔎 Complexity Analysis
- **Worst Case**: If the **largest** element is always chosen as the pivot, it results in **O(n²)**.
- **Average Case**: If an **average pivot** is chosen, we get **O(n log n)**.
- **Best Case**: If the **middle element** is always chosen as the pivot, **O(n log n)** performance is achieved.

### 🚀 Key Takeaways
| Algorithm      | Best Case | Average Case | Worst Case | Space Complexity |
|--------------|----------|-------------|-------------|------------------|
| Selection Sort | **O(n²)** | **O(n²)** | **O(n²)** | **O(1)** |
| Quicksort     | **O(n log n)** | **O(n log n)** | **O(n²)** | **O(n)** (or **O(log n)** with in-place partitioning) |

---

## 📌 Conclusion
- **Selection Sort** is **simple but inefficient** for large datasets due to its **O(n²)** complexity in all cases.
- **Quicksort** is generally **faster** with an average and best-case complexity of **O(n log n)**, but it can degrade to **O(n²)** in the worst case if poor pivot choices are made.
- **Quicksort** is preferred for large datasets due to its divide-and-conquer approach and in-place sorting capability.

🔹 **Use Selection Sort** for **small lists** where simplicity matters.
🔹 **Use Quicksort** for **large lists** where efficiency is required.

Happy Coding! 🚀

