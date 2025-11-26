# Day 22: Đệ quy cơ bản, Base Cases, Recursive Thinking

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Hiểu khái niệm đệ quy và cách thức hoạt động
- Xác định base cases và recursive cases
- Phát triển tư duy đệ quy (recursive thinking)
- Implement các thuật toán đệ quy cơ bản
- Phân tích độ phức tạp của thuật toán đệ quy
- Áp dụng đệ quy vào bài toán Olympic

## Phần 1: Khái niệm đệ quy (45 phút)

### 1.1 Đệ quy là gì?

**Định nghĩa:** Đệ quy là kỹ thuật giải quyết bài toán bằng cách chia nhỏ thành các bài toán con tương tự nhưng đơn giản hơn.

**Cấu trúc đệ quy:**
1. **Base case:** Trường hợp cơ sở, dừng đệ quy
2. **Recursive case:** Trường hợp đệ quy, gọi lại chính nó

```python
def recursive_function(n):
    # Base case - điều kiện dừng
    if n <= 0:
        return "base_result"
    
    # Recursive case - gọi lại chính nó với input nhỏ hơn
    return recursive_function(n - 1)
```

### 1.2 Ví dụ đơn giản - Factorial

```python
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Trace execution:
# factorial(4) = 4 * factorial(3)
#              = 4 * 3 * factorial(2)
#              = 4 * 3 * 2 * factorial(1)
#              = 4 * 3 * 2 * 1
#              = 24
```

### 1.3 Call Stack và Memory

```python
def visualize_recursion(n, depth=0):
    """Visualize recursive calls"""
    indent = "  " * depth
    print(f"{indent}Entering: n={n}")
    
    if n <= 1:
        print(f"{indent}Base case reached: returning 1")
        return 1
    
    result = n * visualize_recursion(n - 1, depth + 1)
    print(f"{indent}Returning: {n} * {result//n} = {result}")
    return result
```

### 1.4 Recursive vs Iterative

```python
# Recursive approach
def sum_recursive(n):
    if n <= 0:
        return 0
    return n + sum_recursive(n - 1)

# Iterative approach
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Mathematical approach
def sum_formula(n):
    return n * (n + 1) // 2
```

## Phần 2: Base Cases và Recursive Cases (45 phút)

### 2.1 Xác định Base Cases

**Nguyên tắc:**
- Base case phải đơn giản, không cần đệ quy
- Phải đảm bảo thuật toán sẽ đạt đến base case
- Có thể có nhiều base cases

```python
def fibonacci(n):
    # Multiple base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

def power(base, exp):
    # Base cases
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if base == 0:
        return 0
    
    # Recursive case
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        return base * power(base, exp - 1)
```

### 2.2 Recursive Case Design

**Nguyên tắc:**
- Input phải giảm dần về base case
- Kết hợp kết quả của subproblems

```python
def gcd(a, b):
    """Greatest Common Divisor using Euclidean algorithm"""
    # Base case
    if b == 0:
        return a
    
    # Recursive case - input giảm dần
    return gcd(b, a % b)

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    # Base case - không tìm thấy
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Base case - tìm thấy
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)
```

### 2.3 Common Recursive Patterns

```python
# Pattern 1: Linear recursion (n -> n-1)
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

# Pattern 2: Binary recursion (n -> n/2)
def binary_search_pattern(n):
    if n <= 1:
        return n
    return binary_search_pattern(n // 2)

# Pattern 3: Multiple recursion (Fibonacci-like)
def tribonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

# Pattern 4: Mutual recursion
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
```

## Phần 3: Recursive Thinking (45 phút)

### 3.1 Cách tiếp cận bài toán đệ quy

**Bước 1:** Xác định bài toán có thể chia nhỏ không?
**Bước 2:** Tìm mối quan hệ giữa bài toán và subproblem
**Bước 3:** Xác định base cases
**Bước 4:** Implement recursive case

```python
def reverse_string_recursive(s):
    """Reverse string using recursion"""
    # Step 1: Can we break it down? Yes - first char + reverse of rest
    # Step 2: reverse(s) = reverse(s[1:]) + s[0]
    # Step 3: Base case - empty or single character
    # Step 4: Implement
    
    if len(s) <= 1:
        return s
    
    return reverse_string_recursive(s[1:]) + s[0]

def palindrome_check_recursive(s):
    """Check if string is palindrome"""
    # Base cases
    if len(s) <= 1:
        return True
    
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Recursive case - check middle part
    return palindrome_check_recursive(s[1:-1])
```

### 3.2 Tree Recursion

```python
def print_all_paths(current_path, remaining_choices):
    """Print all possible paths"""
    # Base case - no more choices
    if not remaining_choices:
        print(current_path)
        return
    
    # Try each remaining choice
    for choice in remaining_choices:
        new_path = current_path + [choice]
        new_remaining = [x for x in remaining_choices if x != choice]
        print_all_paths(new_path, new_remaining)

def generate_parentheses(n):
    """Generate all valid parentheses combinations"""
    def backtrack(current, open_count, close_count):
        # Base case
        if len(current) == 2 * n:
            return [current]
        
        result = []
        
        # Add opening parenthesis
        if open_count < n:
            result.extend(backtrack(current + "(", open_count + 1, close_count))
        
        # Add closing parenthesis
        if close_count < open_count:
            result.extend(backtrack(current + ")", open_count, close_count + 1))
        
        return result
    
    return backtrack("", 0, 0)
```

### 3.3 Recursion với Data Structures

```python
def sum_nested_list(nested_list):
    """Sum all numbers in nested list structure"""
    total = 0
    
    for item in nested_list:
        if isinstance(item, list):
            # Recursive case - item is a list
            total += sum_nested_list(item)
        else:
            # Base case - item is a number
            total += item
    
    return total

def flatten_list(nested_list):
    """Flatten nested list structure"""
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            # Recursive case
            result.extend(flatten_list(item))
        else:
            # Base case
            result.append(item)
    
    return result
```

## Phần 4: Ứng dụng và Tối ưu hóa (45 phút)

### 4.1 Memoization

```python
def fibonacci_memoized(n, memo=None):
    """Fibonacci with memoization"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Using functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)
```

### 4.2 Tail Recursion

```python
def factorial_tail_recursive(n, accumulator=1):
    """Tail recursive factorial"""
    if n <= 1:
        return accumulator
    
    return factorial_tail_recursive(n - 1, n * accumulator)

def sum_tail_recursive(arr, index=0, accumulator=0):
    """Tail recursive sum"""
    if index >= len(arr):
        return accumulator
    
    return sum_tail_recursive(arr, index + 1, accumulator + arr[index])
```

### 4.3 Recursion Depth Limits

```python
import sys

def check_recursion_limit():
    """Check Python's recursion limit"""
    print(f"Current recursion limit: {sys.getrecursionlimit()}")

def safe_deep_recursion(n, limit=900):
    """Safe recursion with depth checking"""
    if n <= 0:
        return 0
    
    if n > limit:
        # Convert to iterative for deep recursion
        return sum(range(1, n + 1))
    
    return n + safe_deep_recursion(n - 1, limit)

# Increase recursion limit if needed (use carefully)
# sys.setrecursionlimit(2000)
```

### 4.4 Debugging Recursive Functions

```python
def debug_recursive_function(func):
    """Decorator to debug recursive calls"""
    def wrapper(*args, **kwargs):
        wrapper.depth = getattr(wrapper, 'depth', 0) + 1
        indent = "  " * (wrapper.depth - 1)
        print(f"{indent}→ {func.__name__}{args}")
        
        result = func(*args, **kwargs)
        
        print(f"{indent}← {func.__name__}{args} = {result}")
        wrapper.depth -= 1
        return result
    
    return wrapper

@debug_recursive_function
def factorial_debug(n):
    if n <= 1:
        return 1
    return n * factorial_debug(n - 1)
```

## Bài tập thực hành

1. **[problem220101.py]** - Basic recursion patterns
2. **[problem220102.py]** - Mathematical recursion
3. **[problem220201.py]** - String recursion
4. **[problem220202.py]** - Array recursion
5. **[problem220301.py]** - Tree recursion và backtracking
6. **[problem220302.py]** - Nested structure recursion
7. **[problem220401.py]** - Recursion optimization
8. **[problem220402.py]** - Advanced recursive problems

## Tổng kết

- Đệ quy chia bài toán thành subproblems nhỏ hơn
- Base cases quan trọng để tránh infinite recursion
- Recursive thinking: tìm pattern và mối quan hệ
- Memoization giúp tối ưu hóa recursive algorithms
- Cần cẩn thận với recursion depth limits
- Debug tools giúp hiểu flow của recursive calls