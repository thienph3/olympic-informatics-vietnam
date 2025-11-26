# Day 5: Recursion Basics

## Recursion Concept và Base Case

### Khái niệm Đệ quy
Đệ quy là kỹ thuật giải quyết vấn đề bằng cách chia nhỏ thành các bài toán con tương tự, cho đến khi đạt được trường hợp cơ sở (base case).

### Cấu trúc cơ bản
```python
def recursive_function(parameters):
    # Base case - điều kiện dừng
    if base_condition:
        return base_value
    
    # Recursive case - gọi chính nó với tham số nhỏ hơn
    return recursive_function(modified_parameters)
```

### Ví dụ đơn giản: Đếm ngược
```python
def countdown(n):
    # Base case
    if n <= 0:
        print("Hết!")
        return
    
    # Recursive case
    print(n)
    countdown(n - 1)

countdown(5)  # In: 5, 4, 3, 2, 1, Hết!
```

## Fibonacci Sequence Implementation

### Fibonacci cơ bản (Naive)
```python
def fibonacci_naive(n):
    """
    Fibonacci naive implementation
    Time complexity: O(2^n) - rất chậm!
    Space complexity: O(n) - call stack
    """
    # Base cases
    if n <= 1:
        return n
    
    # Recursive case
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# Ví dụ
for i in range(10):
    print(f"F({i}) = {fibonacci_naive(i)}")
```

### Fibonacci với Memoization
```python
def fibonacci_memo(n, memo={}):
    """
    Fibonacci với memoization
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Hoặc sử dụng decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
```

### Fibonacci Iterative (Tối ưu nhất)
```python
def fibonacci_iterative(n):
    """
    Fibonacci iterative
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
```

## Factorial Calculation

### Factorial đệ quy
```python
def factorial_recursive(n):
    """
    Tính giai thừa đệ quy
    Time complexity: O(n)
    Space complexity: O(n) - call stack
    """
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # 120
```

### Factorial iterative
```python
def factorial_iterative(n):
    """
    Tính giai thừa iterative
    Time complexity: O(n)
    Space complexity: O(1)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Factorial với xử lý lỗi
```python
def factorial_safe(n):
    """Factorial với xử lý edge cases"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n phải là số nguyên không âm")
    
    if n <= 1:
        return 1
    
    return n * factorial_safe(n - 1)
```

## Common Recursion Patterns

### 1. Linear Recursion
```python
def sum_array(arr, index=0):
    """Tính tổng mảng bằng đệ quy tuyến tính"""
    if index >= len(arr):
        return 0
    return arr[index] + sum_array(arr, index + 1)

def reverse_string(s):
    """Đảo ngược chuỗi"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])
```

### 2. Binary Recursion
```python
def binary_search_recursive(arr, target, left=0, right=None):
    """Binary search đệ quy"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### 3. Multiple Recursion
```python
def tower_of_hanoi(n, source, destination, auxiliary):
    """Tháp Hà Nội"""
    if n == 1:
        print(f"Chuyển đĩa từ {source} sang {destination}")
        return
    
    # Chuyển n-1 đĩa từ source sang auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Chuyển đĩa lớn nhất từ source sang destination
    print(f"Chuyển đĩa từ {source} sang {destination}")
    
    # Chuyển n-1 đĩa từ auxiliary sang destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

tower_of_hanoi(3, 'A', 'C', 'B')
```

### 4. Tail Recursion
```python
def factorial_tail_recursive(n, accumulator=1):
    """Factorial với tail recursion"""
    if n <= 1:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

def gcd_tail_recursive(a, b):
    """GCD với tail recursion"""
    if b == 0:
        return a
    return gcd_tail_recursive(b, a % b)
```

## Tree Recursion Examples

### Tính tổ hợp C(n, k)
```python
def combination(n, k):
    """
    Tính C(n, k) = n! / (k! * (n-k)!)
    Sử dụng công thức: C(n, k) = C(n-1, k-1) + C(n-1, k)
    """
    # Base cases
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    
    # Recursive case
    return combination(n - 1, k - 1) + combination(n - 1, k)

# Với memoization
@lru_cache(maxsize=None)
def combination_memo(n, k):
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    return combination_memo(n - 1, k - 1) + combination_memo(n - 1, k)
```

### Sinh tất cả tập con
```python
def generate_subsets(arr, index=0, current_subset=[]):
    """Sinh tất cả tập con của mảng"""
    # Base case
    if index == len(arr):
        print(current_subset)
        return
    
    # Không chọn phần tử hiện tại
    generate_subsets(arr, index + 1, current_subset)
    
    # Chọn phần tử hiện tại
    generate_subsets(arr, index + 1, current_subset + [arr[index]])

generate_subsets([1, 2, 3])
```

### Sinh hoán vị
```python
def generate_permutations(arr, current_perm=[]):
    """Sinh tất cả hoán vị"""
    # Base case
    if len(current_perm) == len(arr):
        print(current_perm)
        return
    
    # Thử từng phần tử chưa được chọn
    for i in range(len(arr)):
        if arr[i] not in current_perm:
            generate_permutations(arr, current_perm + [arr[i]])

generate_permutations([1, 2, 3])
```

## Recursion vs Iteration

### So sánh hiệu suất
```python
import time
import sys

def compare_fibonacci(n):
    # Tăng recursion limit
    sys.setrecursionlimit(10000)
    
    # Recursive (naive)
    start = time.time()
    result_rec = fibonacci_naive(min(n, 35))  # Giới hạn để tránh quá chậm
    time_rec = time.time() - start
    
    # Iterative
    start = time.time()
    result_iter = fibonacci_iterative(n)
    time_iter = time.time() - start
    
    # Memoized
    start = time.time()
    result_memo = fibonacci_memo(n)
    time_memo = time.time() - start
    
    print(f"n = {n}")
    print(f"Recursive: {time_rec:.6f}s")
    print(f"Iterative: {time_iter:.6f}s")
    print(f"Memoized: {time_memo:.6f}s")

compare_fibonacci(30)
```

### Khi nào dùng đệ quy?
**Ưu điểm:**
- Code ngắn gọn, dễ hiểu
- Tự nhiên với cấu trúc dữ liệu đệ quy (tree, graph)
- Dễ chứng minh tính đúng đắn

**Nhược điểm:**
- Có thể chậm (exponential time)
- Tốn bộ nhớ stack
- Risk of stack overflow

## Ví dụ thực tế

### Bài 1: Tính lũy thừa
```python
def power(base, exp):
    """Tính base^exp bằng đệ quy"""
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    # Tối ưu: chia đôi số mũ
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        return base * power(base, exp - 1)

print(power(2, 10))  # 1024
```

### Bài 2: Tìm UCLN (GCD)
```python
def gcd(a, b):
    """Thuật toán Euclid đệ quy"""
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # 6
```

### Bài 3: Kiểm tra palindrome
```python
def is_palindrome(s, left=0, right=None):
    """Kiểm tra chuỗi palindrome bằng đệ quy"""
    if right is None:
        right = len(s) - 1
    
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return is_palindrome(s, left + 1, right - 1)

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

### Bài 4: Đếm số cách leo cầu thang
```python
def count_ways(n):
    """
    Đếm số cách leo n bậc cầu thang
    Mỗi lần có thể leo 1 hoặc 2 bậc
    """
    if n <= 2:
        return n
    
    return count_ways(n - 1) + count_ways(n - 2)

# Với memoization
@lru_cache(maxsize=None)
def count_ways_memo(n):
    if n <= 2:
        return n
    return count_ways_memo(n - 1) + count_ways_memo(n - 2)

print(count_ways_memo(10))  # 89
```

## Best Practices

1. **Luôn có base case** để tránh infinite recursion
2. **Đảm bảo tiến tới base case** ở mỗi recursive call
3. **Sử dụng memoization** cho overlapping subproblems
4. **Cân nhắc iterative solution** nếu performance quan trọng
5. **Kiểm tra recursion depth** với input lớn
6. **Tail recursion optimization** khi có thể