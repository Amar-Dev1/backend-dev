# 📌 Algorithmic Paradigms


## ⚡ 1. Divide and Conquer
**Divide and Conquer** is a problem-solving technique that breaks a problem into smaller subproblems, solves them recursively, and then combines their solutions.

### ✅ **Steps**:
1. **Divide**: Break the problem into smaller subproblems.
2. **Conquer**: Solve each subproblem recursively.
3. **Combine**: Merge the solutions to get the final result. (optional step)

### 📌 **Example: Merge Sort**
- **Divide**: Split the array into two halves.
- **Conquer**: Recursively sort each half.
- **Combine**: Merge the sorted halves.

**Time Complexity:** O(n log n) due to repeated splitting and merging.

---

## 🔄 2. Recursion
Recursion is a technique where a function calls itself to solve smaller instances of a problem.

### ✅ **Steps**:
1. Define a **base case** (stopping condition).
2. Define the **recursive case** (where the function calls itself with a smaller input).

### 📌 **Example: Factorial Calculation**
```python
# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive call
```
**Time Complexity:** O(n) as it makes n recursive calls.

---

## 🎯 3. Dynamic Programming (DP)
Dynamic Programming is used to solve problems by **breaking them into overlapping subproblems** and storing the results to avoid redundant calculations.

### ✅ **Steps**:
1. **Identify** overlapping subproblems.
2. **Store** the results of solved subproblems (Memoization/Table).
3. **Use** stored results to solve larger problems efficiently.

- 💡 Memoization: memoization is an optimization technique used in Dynamic Programming to store previously computed results and reuse them to avoid redundant calculations.

### 📌 **Example: Fibonacci Sequence**
```python
# Fibonacci with memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```
**Time Complexity:** O(n) due to memoization, reducing redundant calculations.

---

## 💰 4. Greedy Algorithms
A **Greedy Algorithm** builds the solution piece by piece, always choosing the locally optimal choice at each step.

### ✅ **Steps**:
1. **Choose** the best possible option at the current step.
2. **Repeat** for the remaining problem.
3. **Obtain** the final solution (not always optimal globally).

### 📌 **Example: Coin Change Problem**
- Given coins `{1, 5, 10, 25}`, minimize the number of coins to make an amount.
- Always pick the largest possible coin first.

**Time Complexity:** O(n) (depends on the problem and implementation).

---

### 🚀 **Key Takeaways**:
- **Divide and Conquer** efficiently breaks down and combines problems.
- **Recursion** solves problems by self-referencing functions.
- **Dynamic Programming** avoids redundant work using memoization.
- **Greedy Algorithms** make local choices, sometimes leading to suboptimal results.

🔹 **Choosing the right paradigm depends on the problem’s nature!**

