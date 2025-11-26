# Day 20: Độ phức tạp thuật toán, Big O notation

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Hiểu khái niệm độ phức tạp thời gian và không gian
- Thành thạo Big O notation và các ký hiệu asymptotic
- Phân tích độ phức tạp của thuật toán và cấu trúc dữ liệu
- So sánh hiệu suất các thuật toán khác nhau
- Áp dụng kiến thức vào tối ưu hóa code trong Olympic

## Phần 1: Khái niệm cơ bản về độ phức tạp (45 phút)

### 1.1 Tại sao cần phân tích độ phức tạp?

**Mục đích:**
- Dự đoán hiệu suất thuật toán với input lớn
- So sánh các thuật toán khác nhau
- Tối ưu hóa code cho Olympic (time limit)
- Ước lượng memory usage

**Ví dụ thực tế:**
```python
# Thuật toán O(n²) - chậm với n lớn
def find_duplicates_slow(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Thuật toán O(n) - nhanh hơn nhiều
def find_duplicates_fast(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
```

### 1.2 Time Complexity vs Space Complexity

**Time Complexity:** Thời gian thực thi theo kích thước input
**Space Complexity:** Bộ nhớ sử dụng theo kích thước input

```python
def example_time_space():
    # O(1) time, O(1) space
    def constant_example(n):
        return n * 2
    
    # O(n) time, O(1) space
    def linear_time_constant_space(arr):
        total = 0
        for num in arr:
            total += num
        return total
    
    # O(n) time, O(n) space
    def linear_time_space(arr):
        return [x * 2 for x in arr]
    
    # O(n²) time, O(1) space
    def quadratic_time_constant_space(arr):
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count += 1
        return count
```

## Phần 2: Big O Notation và Asymptotic Analysis (45 phút)

### 2.1 Các ký hiệu Asymptotic

**Big O (O):** Upper bound - worst case
**Big Omega (Ω):** Lower bound - best case  
**Big Theta (Θ):** Tight bound - average case

### 2.2 Các độ phức tạp phổ biến

```python
# O(1) - Constant time
def constant_time(arr):
    return arr[0] if arr else None

# O(log n) - Logarithmic time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear time
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# O(n log n) - Linearithmic time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# O(n²) - Quadratic time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(2ⁿ) - Exponential time
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# O(n!) - Factorial time
def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]] + perm)
    return result
```

### 2.3 Bảng so sánh độ phức tạp

| Complexity | n=10 | n=100 | n=1000 | n=10000 | Growth Rate |
|------------|------|-------|--------|---------|-------------|
| O(1) | 1 | 1 | 1 | 1 | Excellent |
| O(log n) | 3 | 7 | 10 | 13 | Excellent |
| O(n) | 10 | 100 | 1000 | 10000 | Good |
| O(n log n) | 30 | 700 | 10000 | 130000 | Good |
| O(n²) | 100 | 10000 | 1000000 | 100000000 | Poor |
| O(2ⁿ) | 1024 | 2³⁰ | 2¹⁰⁰⁰ | 2¹⁰⁰⁰⁰ | Terrible |

## Phần 3: Phân tích độ phức tạp của thuật toán (45 phút)

### 3.1 Quy tắc phân tích

**1. Drop constants:** O(2n) → O(n)
**2. Drop non-dominant terms:** O(n² + n) → O(n²)
**3. Different inputs use different variables:** O(a + b)

```python
def analyze_complexity_examples():
    # O(n) - single loop
    def example1(arr):
        for item in arr:  # n iterations
            print(item)   # O(1) operation
        # Total: O(n)
    
    # O(n²) - nested loops
    def example2(arr):
        for i in range(len(arr)):      # n iterations
            for j in range(len(arr)):  # n iterations each
                print(arr[i], arr[j])  # O(1) operation
        # Total: O(n²)
    
    # O(n) - two separate loops
    def example3(arr1, arr2):
        for item in arr1:  # n iterations
            print(item)
        for item in arr2:  # m iterations
            print(item)
        # Total: O(n + m)
    
    # O(log n) - divide by 2 each time
    def example4(n):
        while n > 1:
            print(n)
            n = n // 2
        # Total: O(log n)
    
    # O(n log n) - loop with divide
    def example5(arr):
        for i in range(len(arr)):  # n iterations
            n = len(arr)
            while n > 1:           # log n iterations
                print(n)
                n = n // 2
        # Total: O(n log n)
```

### 3.2 Phân tích đệ quy

```python
def analyze_recursive_complexity():
    # T(n) = T(n-1) + O(1) → O(n)
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    # T(n) = 2T(n-1) + O(1) → O(2ⁿ)
    def fibonacci_bad(n):
        if n <= 1:
            return n
        return fibonacci_bad(n - 1) + fibonacci_bad(n - 2)
    
    # T(n) = T(n-1) + O(1) → O(n) with memoization
    def fibonacci_good(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci_good(n - 1, memo) + fibonacci_good(n - 2, memo)
        return memo[n]
    
    # T(n) = 2T(n/2) + O(n) → O(n log n)
    def merge_sort_analysis(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_analysis(arr[:mid])    # T(n/2)
        right = merge_sort_analysis(arr[mid:])   # T(n/2)
        return merge(left, right)                # O(n)
```

## Phần 4: Độ phức tạp của cấu trúc dữ liệu (45 phút)

### 4.1 Array/List Operations

```python
# Python List complexity
operations = {
    'Access by index': 'O(1)',
    'Search': 'O(n)',
    'Insert at end': 'O(1) amortized',
    'Insert at beginning': 'O(n)',
    'Delete at end': 'O(1)',
    'Delete at beginning': 'O(n)',
    'Delete by value': 'O(n)'
}
```

### 4.2 Dictionary/Hash Table

```python
# Python Dict complexity
dict_operations = {
    'Access by key': 'O(1) average, O(n) worst',
    'Insert': 'O(1) average, O(n) worst',
    'Delete': 'O(1) average, O(n) worst',
    'Search': 'O(1) average, O(n) worst'
}
```

### 4.3 Set Operations

```python
# Python Set complexity
set_operations = {
    'Add': 'O(1) average',
    'Remove': 'O(1) average',
    'Contains': 'O(1) average',
    'Union': 'O(len(s1) + len(s2))',
    'Intersection': 'O(min(len(s1), len(s2)))'
}
```

### 4.4 Sorting Algorithms Comparison

```python
sorting_complexity = {
    'Bubble Sort': {'Time': 'O(n²)', 'Space': 'O(1)'},
    'Selection Sort': {'Time': 'O(n²)', 'Space': 'O(1)'},
    'Insertion Sort': {'Time': 'O(n²)', 'Space': 'O(1)'},
    'Merge Sort': {'Time': 'O(n log n)', 'Space': 'O(n)'},
    'Quick Sort': {'Time': 'O(n log n) avg, O(n²) worst', 'Space': 'O(log n)'},
    'Heap Sort': {'Time': 'O(n log n)', 'Space': 'O(1)'},
    'Counting Sort': {'Time': 'O(n + k)', 'Space': 'O(k)'},
    'Radix Sort': {'Time': 'O(d(n + k))', 'Space': 'O(n + k)'}
}
```

### 4.5 Ứng dụng trong Olympic

```python
def olympic_time_limits():
    """
    Ước lượng thuật toán phù hợp với time limit
    """
    time_limits = {
        '1 second': {
            'n ≤ 10⁸': 'O(1), O(log n)',
            'n ≤ 10⁶': 'O(n)',
            'n ≤ 10⁴': 'O(n log n)',
            'n ≤ 10³': 'O(n²)',
            'n ≤ 20': 'O(2ⁿ)',
            'n ≤ 10': 'O(n!)'
        },
        '2 seconds': {
            'n ≤ 2×10⁸': 'O(1), O(log n)',
            'n ≤ 2×10⁶': 'O(n)',
            'n ≤ 2×10⁴': 'O(n log n)',
            'n ≤ 1.4×10³': 'O(n²)'
        }
    }
    return time_limits

def choose_algorithm_by_constraints(n, time_limit):
    """
    Chọn thuật toán dựa trên constraints
    """
    if n <= 20 and time_limit >= 1:
        return "Có thể dùng O(2ⁿ) hoặc O(n!)"
    elif n <= 1000 and time_limit >= 1:
        return "Có thể dùng O(n²)"
    elif n <= 10000 and time_limit >= 1:
        return "Nên dùng O(n log n)"
    elif n <= 1000000 and time_limit >= 1:
        return "Nên dùng O(n)"
    else:
        return "Cần thuật toán O(1) hoặc O(log n)"
```

## Bài tập thực hành

1. **[problem200101.py]** - Basic complexity analysis
2. **[problem200102.py]** - Time complexity measurement
3. **[problem200201.py]** - Space complexity analysis
4. **[problem200202.py]** - Recursive complexity analysis
5. **[problem200301.py]** - Data structure complexity
6. **[problem200302.py]** - Algorithm comparison
7. **[problem200401.py]** - Optimization techniques
8. **[problem200402.py]** - Olympic problem analysis

## Tổng kết

- Big O notation mô tả growth rate của thuật toán
- Focus vào worst case và input size lớn
- Drop constants và non-dominant terms
- Hiểu complexity của built-in operations
- Chọn thuật toán phù hợp với constraints của bài toán
- Trong Olympic: O(n²) thường chỉ work với n ≤ 10³-10⁴