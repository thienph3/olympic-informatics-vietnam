# Day 11: Function nâng cao - lambda, scope, recursion

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Lambda functions (45')

### 📚 Lý thuyết (15')

#### Khái niệm Lambda
```python
# Lambda = anonymous function (hàm ẩn danh)
# Cú pháp: lambda arguments: expression

# Function thường
def square(x):
    return x ** 2

# Lambda tương đương
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# Lambda với nhiều tham số
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda với conditional
max_lambda = lambda x, y: x if x > y else y
print(max_lambda(10, 5))  # 10
```

#### Lambda với built-in functions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() với lambda
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter() với lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# sorted() với lambda
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)  # [('Charlie', 78), ('Alice', 85), ('Bob', 90)]

# reduce() với lambda
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)  # 120
```

#### Lambda limitations
```python
# Lambda chỉ có thể chứa expression, không có statement
# KHÔNG thể làm:
# lambda x: print(x)  # print là statement
# lambda x: if x > 0: return x  # if statement

# Thay vào đó:
print_lambda = lambda x: x  # return value để print bên ngoài
conditional_lambda = lambda x: x if x > 0 else 0  # conditional expression

# Lambda không có docstring
# Lambda khó debug
# Lambda nên đơn giản, ngắn gọn
```

### 💻 Thực hành (30')

#### Bài tập 1: Lambda cơ bản với map, filter, sorted

**Yêu cầu:** Sử dụng lambda với các built-in functions để xử lý dữ liệu.

**File thực hành:** [problem110101.py](problem110101.py)

#### Bài tập 2: Lambda trong data processing

**Yêu cầu:** Áp dụng lambda cho xử lý dữ liệu phức tạp và functional programming.

**File thực hành:** [problem110102.py](problem110102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Higher-order functions và Closures (45')

### 📚 Lý thuyết (20')

#### Higher-order functions
```python
# Function nhận function khác làm parameter
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
print(apply_operation(numbers, square))  # [1, 4, 9, 16, 25]
print(apply_operation(numbers, cube))    # [1, 8, 27, 64, 125]

# Function trả về function khác
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

#### Closures
```python
# Closure = function + enclosing scope variables
def outer_function(x):
    # Enclosing scope variable
    def inner_function(y):
        return x + y  # x từ outer scope
    return inner_function

add_10 = outer_function(10)
print(add_10(5))  # 15

# Closure với mutable variables
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (independent counter)
```

#### Decorators cơ bản
```python
# Decorator = function modifier
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# Sử dụng decorator
@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Before function call
# Hello, Alice!
# After function call

# Decorator với parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" 3 times
```

#### Functional programming concepts
```python
# Partial functions
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)  # Fix first argument to 2
print(double(5))  # 10

# Function composition
def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

# Compose functions
add_then_multiply = compose(multiply_by_two, add_one)
print(add_then_multiply(5))  # (5 + 1) * 2 = 12
```

### 💻 Thực hành (25')

#### Bài tập 1: Higher-order functions và closures

**Yêu cầu:** Tạo higher-order functions, closures và decorators đơn giản.

**File thực hành:** [problem110201.py](problem110201.py)

#### Bài tập 2: Functional programming patterns

**Yêu cầu:** Áp dụng functional programming: partial functions, composition, currying.

**File thực hành:** [problem110202.py](problem110202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Recursion cơ bản (45')

### 📚 Lý thuyết (15')

#### Khái niệm Recursion
```python
# Recursion = function gọi chính nó
# Cần có: base case + recursive case

def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 5! = 120

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8

# Countdown example
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)  # 5, 4, 3, 2, 1, Done!
```

#### Recursion vs Iteration
```python
# Factorial - Recursive
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Factorial - Iterative
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Sum of list - Recursive
def sum_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

# Sum of list - Iterative
def sum_iterative(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Recursion: elegant but can be slower, stack overflow risk
# Iteration: faster, more memory efficient
```

#### Common recursion patterns
```python
# Linear recursion
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Binary recursion
def fibonacci_binary(n):
    if n <= 1:
        return n
    return fibonacci_binary(n - 1) + fibonacci_binary(n - 2)

# Tail recursion (Python doesn't optimize this)
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n - 1, n * acc)

# Multiple recursion
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        tower_of_hanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n - 1, auxiliary, destination, source)
```

### 💻 Thực hành (30')

#### Bài tập 1: Recursion cơ bản

**Yêu cầu:** Implement các functions đệ quy: factorial, fibonacci, power, sum.

**File thực hành:** [problem110301.py](problem110301.py)

#### Bài tập 2: Recursion với data structures

**Yêu cầu:** Sử dụng đệ quy để xử lý lists, strings và nested structures.

**File thực hành:** [problem110302.py](problem110302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Advanced Recursion và Olympic Applications (45')

### 📚 Lý thuyết (15')

#### Memoization
```python
# Memoization = cache kết quả để tránh tính lại
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Using functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print(fibonacci_cached(50))  # Fast!
```

#### Backtracking
```python
# Backtracking = try all possibilities, backtrack if dead end
def generate_permutations(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in generate_permutations(rest):
            result.append([arr[i]] + perm)
    
    return result

print(generate_permutations([1, 2, 3]))

# N-Queens problem (simplified)
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        
        return True
    
    def backtrack(board, row):
        if row == n:
            return [board[:]]
        
        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solutions.extend(backtrack(board, row + 1))
                board[row] = -1  # backtrack
        
        return solutions
    
    return backtrack([-1] * n, 0)
```

#### Divide and Conquer
```python
# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Binary Search (recursive)
def binary_search_recursive(arr, target, left=0, right=None):
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

#### Tree Traversal
```python
# Binary Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree traversals
def inorder_traversal(root):
    if not root:
        return []
    return (inorder_traversal(root.left) + 
            [root.val] + 
            inorder_traversal(root.right))

def preorder_traversal(root):
    if not root:
        return []
    return ([root.val] + 
            preorder_traversal(root.left) + 
            preorder_traversal(root.right))

def postorder_traversal(root):
    if not root:
        return []
    return (postorder_traversal(root.left) + 
            postorder_traversal(root.right) + 
            [root.val])

def tree_height(root):
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))
```

### 💻 Thực hành (30')

#### Bài tập 1: Memoization và optimization

**Yêu cầu:** Implement memoization, compare performance, optimize recursive solutions.

**File thực hành:** [problem110401.py](problem110401.py)

#### Bài tập 2: Backtracking và divide-and-conquer

**Yêu cầu:** Solve problems using backtracking và divide-and-conquer techniques.

**File thực hành:** [problem110402.py](problem110402.py)

---

## Bài tập về nhà

### Bài 1: Advanced Lambda Applications
Sử dụng lambda cho:
- Custom sorting với multiple criteria
- Data transformation pipelines
- Event handling systems
- Functional programming patterns

### Bài 2: Recursive Problem Solving
Giải các bài toán đệ quy:
- Generate all subsets of a set
- Solve Sudoku puzzle
- Find all paths in a maze
- Calculate edit distance recursively

### Bài 3: Performance Analysis
So sánh hiệu suất:
- Recursive vs iterative implementations
- Memoized vs non-memoized recursion
- Different sorting algorithms
- Space complexity analysis

### Gợi ý làm bài
1. Sử dụng lambda cho các operations đơn giản
2. Apply memoization cho recursive functions
3. Identify base cases carefully
4. Consider iterative alternatives for deep recursion

---

## Tổng kết Day 11

**Đã học:**
- Lambda functions: anonymous functions, functional programming
- Higher-order functions và closures
- Decorators cơ bản và function composition
- Recursion: base case, recursive case, patterns
- Memoization và optimization techniques
- Backtracking và divide-and-conquer
- Tree traversal và recursive data structures
- Performance considerations

**Chuẩn bị cho Day 12:**
- Ôn lại recursion và lambda functions
- Thực hành backtracking problems
- Làm xong bài tập về nhà
- Chuẩn bị học Modules và File I/O