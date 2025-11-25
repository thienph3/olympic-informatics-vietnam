"""
Problem 110301: Recursion cơ bản
Implement các functions đệ quy: factorial, fibonacci, power, sum

Bài 1: Basic Recursive Functions
- Factorial, Fibonacci, Power
- Sum và Product của lists
- String operations

Bài 2: Recursive Data Structure Processing
- List processing
- Nested structure traversal
- Tree-like operations
"""

# Basic Recursive Functions
def factorial_recursive(n):
    """Tính giai thừa đệ quy"""
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial_recursive(n - 1)

def fibonacci_recursive(n):
    """Tính Fibonacci đệ quy (naive)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def power_recursive(base, exp):
    """Tính lũy thừa đệ quy"""
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power_recursive(base, exp - 1)

def power_optimized(base, exp):
    """Tính lũy thừa đệ quy tối ưu (fast exponentiation)"""
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    if exp % 2 == 0:
        half_power = power_optimized(base, exp // 2)
        return half_power * half_power
    else:
        return base * power_optimized(base, exp - 1)

def sum_recursive(numbers):
    """Tính tổng list đệ quy"""
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

def product_recursive(numbers):
    """Tính tích list đệ quy"""
    if not numbers:
        return 1
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] * product_recursive(numbers[1:])

def gcd_recursive(a, b):
    """Tính GCD đệ quy (Euclidean algorithm)"""
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)

def count_digits_recursive(n):
    """Đếm số chữ số đệ quy"""
    if n == 0:
        return 1
    if abs(n) < 10:
        return 1
    return 1 + count_digits_recursive(abs(n) // 10)

def reverse_number_recursive(n, reversed_num=0):
    """Đảo ngược số đệ quy"""
    if n == 0:
        return reversed_num
    return reverse_number_recursive(n // 10, reversed_num * 10 + n % 10)

def is_palindrome_recursive(s, start=0, end=None):
    """Kiểm tra palindrome đệ quy"""
    if end is None:
        end = len(s) - 1
    
    if start >= end:
        return True
    
    if s[start] != s[end]:
        return False
    
    return is_palindrome_recursive(s, start + 1, end - 1)

# String Operations
def reverse_string_recursive(s):
    """Đảo ngược string đệ quy"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

def count_char_recursive(s, char):
    """Đếm ký tự trong string đệ quy"""
    if not s:
        return 0
    count = 1 if s[0] == char else 0
    return count + count_char_recursive(s[1:], char)

def remove_char_recursive(s, char):
    """Xóa ký tự khỏi string đệ quy"""
    if not s:
        return ""
    if s[0] == char:
        return remove_char_recursive(s[1:], char)
    else:
        return s[0] + remove_char_recursive(s[1:], char)

# List Processing
def find_max_recursive(numbers):
    """Tìm max trong list đệ quy"""
    if len(numbers) == 1:
        return numbers[0]
    
    max_rest = find_max_recursive(numbers[1:])
    return numbers[0] if numbers[0] > max_rest else max_rest

def find_min_recursive(numbers):
    """Tìm min trong list đệ quy"""
    if len(numbers) == 1:
        return numbers[0]
    
    min_rest = find_min_recursive(numbers[1:])
    return numbers[0] if numbers[0] < min_rest else min_rest

def linear_search_recursive(arr, target, index=0):
    """Tìm kiếm tuyến tính đệ quy"""
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

def binary_search_recursive(arr, target, left=0, right=None):
    """Tìm kiếm nhị phân đệ quy"""
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

def flatten_list_recursive(nested_list):
    """Flatten nested list đệ quy"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list_recursive(item))
        else:
            result.append(item)
    return result

def deep_copy_recursive(obj):
    """Deep copy đệ quy cho nested structures"""
    if isinstance(obj, list):
        return [deep_copy_recursive(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: deep_copy_recursive(value) for key, value in obj.items()}
    elif isinstance(obj, tuple):
        return tuple(deep_copy_recursive(item) for item in obj)
    else:
        return obj

# Mathematical Sequences
def triangular_number_recursive(n):
    """Tính số tam giác thứ n đệ quy"""
    if n <= 1:
        return n
    return n + triangular_number_recursive(n - 1)

def catalan_number_recursive(n):
    """Tính số Catalan thứ n đệ quy"""
    if n <= 1:
        return 1
    
    result = 0
    for i in range(n):
        result += catalan_number_recursive(i) * catalan_number_recursive(n - 1 - i)
    return result

def ackermann_function(m, n):
    """Hàm Ackermann - ví dụ về recursion sâu"""
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann_function(m - 1, 1)
    else:
        return ackermann_function(m - 1, ackermann_function(m, n - 1))

# Performance Comparison
def compare_recursive_iterative():
    """So sánh hiệu suất recursive vs iterative"""
    import time
    
    def factorial_iterative(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def fibonacci_iterative(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    # Test factorial
    n = 10
    
    start = time.time()
    result_rec = factorial_recursive(n)
    time_rec = time.time() - start
    
    start = time.time()
    result_iter = factorial_iterative(n)
    time_iter = time.time() - start
    
    print(f"Factorial({n}):")
    print(f"  Recursive: {result_rec} ({time_rec:.6f}s)")
    print(f"  Iterative: {result_iter} ({time_iter:.6f}s)")
    
    # Test fibonacci (smaller n due to exponential complexity)
    n = 20
    
    start = time.time()
    result_rec = fibonacci_recursive(n)
    time_rec = time.time() - start
    
    start = time.time()
    result_iter = fibonacci_iterative(n)
    time_iter = time.time() - start
    
    print(f"\nFibonacci({n}):")
    print(f"  Recursive: {result_rec} ({time_rec:.6f}s)")
    print(f"  Iterative: {result_iter} ({time_iter:.6f}s)")

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Basic Recursive Functions ===")
    
    # Test factorial
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) = {factorial_recursive(n)}")
    
    # Test fibonacci
    print(f"\nFibonacci sequence:")
    for i in range(10):
        print(f"F({i}) = {fibonacci_recursive(i)}")
    
    # Test power
    print(f"\nPower functions:")
    print(f"2^8 = {power_recursive(2, 8)}")
    print(f"2^8 (optimized) = {power_optimized(2, 8)}")
    
    # Test list operations
    numbers = [1, 2, 3, 4, 5]
    print(f"\nList operations on {numbers}:")
    print(f"Sum: {sum_recursive(numbers)}")
    print(f"Product: {product_recursive(numbers)}")
    print(f"Max: {find_max_recursive(numbers)}")
    print(f"Min: {find_min_recursive(numbers)}")
    
    # Test GCD
    print(f"\nGCD(48, 18) = {gcd_recursive(48, 18)}")
    
    # Test number operations
    n = 12345
    print(f"\nNumber operations on {n}:")
    print(f"Digit count: {count_digits_recursive(n)}")
    print(f"Reversed: {reverse_number_recursive(n)}")
    
    print("\n=== Bài 2: String và List Processing ===")
    
    # Test string operations
    text = "hello"
    print(f"String operations on '{text}':")
    print(f"Reversed: '{reverse_string_recursive(text)}'")
    print(f"Count 'l': {count_char_recursive(text, 'l')}")
    print(f"Remove 'l': '{remove_char_recursive(text, 'l')}'")
    
    # Test palindrome
    test_strings = ["racecar", "hello", "madam"]
    for s in test_strings:
        print(f"'{s}' is palindrome: {is_palindrome_recursive(s)}")
    
    # Test search
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"\nSearch {target} in {arr}:")
    print(f"Linear search: index {linear_search_recursive(arr, target)}")
    print(f"Binary search: index {binary_search_recursive(arr, target)}")
    
    # Test nested structures
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"\nNested list: {nested}")
    print(f"Flattened: {flatten_list_recursive(nested)}")
    
    # Test mathematical sequences
    print(f"\nMathematical sequences:")
    for i in range(6):
        print(f"Triangular({i}) = {triangular_number_recursive(i)}")
    
    for i in range(5):
        print(f"Catalan({i}) = {catalan_number_recursive(i)}")
    
    # Performance comparison
    print(f"\n=== Performance Comparison ===")
    compare_recursive_iterative()

    print("\n=== Bài tập thực hành ===")
    print("1. Implement merge sort recursively")
    print("2. Solve Tower of Hanoi problem")
    print("3. Generate all permutations of a string")
    print("4. Calculate tree height recursively")