# Day 10: Function cơ bản - parameters, return values

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Function cơ bản (45')

### 📚 Lý thuyết (15')

#### Khái niệm Function
```python
# Function là khối code có thể tái sử dụng
# Giúp tổ chức code, tránh lặp lại

# Định nghĩa function
def greet():
    print("Hello, World!")

# Gọi function
greet()  # Output: Hello, World!

# Function với docstring
def calculate_area():
    """Tính diện tích hình vuông 5x5"""
    return 5 * 5

print(calculate_area())  # 25
```

#### Function với parameters
```python
# Parameter vs Argument
def greet_person(name):  # name là parameter
    print(f"Hello, {name}!")

greet_person("Alice")  # "Alice" là argument

# Nhiều parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8

# Parameters với kiểu dữ liệu khác nhau
def display_info(name, age, is_student):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Student: {is_student}")

display_info("Bob", 20, True)
```

#### Return statement
```python
# Function không return (return None)
def print_message(msg):
    print(msg)

result = print_message("Hello")
print(result)  # None

# Function có return
def multiply(x, y):
    return x * y

product = multiply(4, 5)
print(product)  # 20

# Multiple return values
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
print(f"{name} is {age} years old")

# Early return
def check_positive(number):
    if number <= 0:
        return False
    return True
```

### 💻 Thực hành (30')

#### Bài tập 1: Function cơ bản và parameters

**Yêu cầu:** Tạo functions đơn giản với parameters và return values.

**File thực hành:** [problem100101.py](problem100101.py)

#### Bài tập 2: Functions cho tính toán

**Yêu cầu:** Viết functions tính toán: diện tích, chu vi, phép toán cơ bản.

**File thực hành:** [problem100102.py](problem100102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Default parameters và keyword arguments (45')

### 📚 Lý thuyết (20')

#### Default parameters
```python
# Giá trị mặc định cho parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
print(greet("Charlie", "Hey"))  # Hey, Charlie!

# Multiple default parameters
def create_profile(name, age=18, city="Unknown"):
    return f"{name}, {age} years old, from {city}"

print(create_profile("Alice"))
print(create_profile("Bob", 25))
print(create_profile("Charlie", 30, "Hanoi"))
```

#### Keyword arguments
```python
# Gọi function với keyword arguments
def introduce(name, age, city):
    return f"I'm {name}, {age} years old, from {city}"

# Positional arguments
print(introduce("Alice", 25, "Hanoi"))

# Keyword arguments
print(introduce(name="Bob", age=30, city="HCMC"))
print(introduce(age=22, city="Danang", name="Charlie"))

# Mixed arguments
print(introduce("David", age=28, city="Hue"))
```

#### *args và **kwargs cơ bản
```python
# *args - variable positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - variable keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Hanoi")
print_info(course="Python", level="Beginner")
```

#### Mutable default arguments (CẢNH BÁO)
```python
# SAIIIIII - Không làm như này!
def add_item_wrong(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item_wrong("apple"))   # ['apple']
print(add_item_wrong("banana"))  # ['apple', 'banana'] - BUG!

# ĐÚNG - Làm như này
def add_item_correct(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item_correct("apple"))   # ['apple']
print(add_item_correct("banana"))  # ['banana'] - ĐÚNG!
```

### 💻 Thực hành (25')

#### Bài tập 1: Default parameters và keyword arguments

**Yêu cầu:** Thực hành default parameters, keyword arguments và *args/**kwargs.

**File thực hành:** [problem100201.py](problem100201.py)

#### Bài tập 2: Functions với tham số linh hoạt

**Yêu cầu:** Tạo functions xử lý số lượng tham số thay đổi.

**File thực hành:** [problem100202.py](problem100202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Local và Global scope (45')

### 📚 Lý thuyết (15')

#### Local scope
```python
# Biến local chỉ tồn tại trong function
def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()  # I'm local
# print(local_var)  # NameError!

# Parameters cũng là local variables
def greet(name):  # name là local variable
    message = f"Hello, {name}"  # message cũng là local
    return message

print(greet("Alice"))
# print(name)     # NameError!
# print(message)  # NameError!
```

#### Global scope
```python
# Biến global có thể truy cập từ mọi nơi
global_var = "I'm global"

def access_global():
    print(global_var)  # Có thể đọc global variable

def modify_global():
    global global_var  # Cần từ khóa global để modify
    global_var = "Modified global"

print(global_var)    # I'm global
access_global()      # I'm global
modify_global()
print(global_var)    # Modified global
```

#### LEGB Rule
```python
# Local -> Enclosing -> Global -> Built-in
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"Inner: {x}")  # local
    
    inner()
    print(f"Outer: {x}")  # enclosing

outer()
print(f"Global: {x}")  # global

# Built-in example
def test_builtin():
    print(len([1, 2, 3]))  # len là built-in function

test_builtin()
```

#### Nonlocal keyword
```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Truy cập biến của outer function
        x = "modified by inner"
        print(f"Inner: {x}")
    
    print(f"Before: {x}")
    inner()
    print(f"After: {x}")

outer()
# Before: outer
# Inner: modified by inner  
# After: modified by inner
```

### 💻 Thực hành (30')

#### Bài tập 1: Scope và variable access

**Yêu cầu:** Thực hành local/global scope, LEGB rule và nonlocal.

**File thực hành:** [problem100301.py](problem100301.py)

#### Bài tập 2: Quản lý state với global variables

**Yêu cầu:** Sử dụng global variables để quản lý trạng thái chương trình.

**File thực hành:** [problem100302.py](problem100302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Functions trong Olympic Programming (45')

### 📚 Lý thuyết (15')

#### Mathematical functions
```python
import math

def gcd(a, b):
    """Tính ước chung lớn nhất"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Tính bội chung nhỏ nhất"""
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Tính giai thừa"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

#### Array processing functions
```python
def find_max_subarray_sum(arr):
    """Kadane's algorithm - tìm tổng dãy con lớn nhất"""
    max_sum = current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def binary_search(arr, target):
    """Tìm kiếm nhị phân"""
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

def merge_sorted_arrays(arr1, arr2):
    """Trộn 2 mảng đã sắp xếp"""
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
```

#### String processing functions
```python
def is_palindrome(s):
    """Kiểm tra chuỗi palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_words(text):
    """Đếm từ trong văn bản"""
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip(".,!?")
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def longest_common_prefix(strs):
    """Tìm tiền tố chung dài nhất"""
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

#### Input/Output helper functions
```python
def read_integers():
    """Đọc dòng số nguyên"""
    return list(map(int, input().split()))

def read_matrix(rows):
    """Đọc ma trận"""
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """In ma trận"""
    for row in matrix:
        print(" ".join(map(str, row)))

def format_output(result):
    """Format kết quả cho Olympic"""
    if isinstance(result, list):
        return " ".join(map(str, result))
    return str(result)
```

### 💻 Thực hành (30')

#### Bài tập 1: Mathematical functions cho Olympic

**Yêu cầu:** Implement các functions toán học: GCD, LCM, prime check, factorial.

**File thực hành:** [problem100401.py](problem100401.py)

#### Bài tập 2: Algorithm functions cho competitive programming

**Yêu cầu:** Viết functions cho thuật toán: binary search, array processing, string algorithms.

**File thực hành:** [problem100402.py](problem100402.py)

---

## Bài tập về nhà

### Bài 1: Calculator Functions
Viết chương trình máy tính với functions:
- Các phép toán cơ bản (+, -, *, /, %, **)
- Phép toán nâng cao (sqrt, sin, cos, log)
- Chuyển đổi số (binary, octal, hex)
- Lịch sử tính toán
- Menu điều khiển

### Bài 2: Number Theory Functions
Implement các functions lý thuyết số:
- Sàng Eratosthenes tìm số nguyên tố
- Phân tích thừa số nguyên tố
- Tính Euler's totient function φ(n)
- Kiểm tra số hoàn hảo, số thân thiện
- Tìm nghiệm phương trình Diophantine

### Bài 3: String Processing Library
Tạo thư viện xử lý chuỗi:
- Các thuật toán pattern matching
- Text analysis (frequency, readability)
- String compression/decompression
- Caesar cipher và Vigenère cipher
- Anagram solver

### Gợi ý làm bài
1. Chia nhỏ bài toán thành các functions riêng biệt
2. Sử dụng docstring để mô tả function
3. Test functions với nhiều test cases
4. Tối ưu hóa thuật toán cho competitive programming

---

## Tổng kết Day 10

**Đã học:**
- Function cơ bản: định nghĩa, parameters, return values
- Default parameters và keyword arguments
- *args và **kwargs cho tham số linh hoạt
- Local và Global scope, LEGB rule
- Nonlocal keyword cho nested functions
- Functions trong Olympic Programming
- Mathematical và algorithmic functions
- Input/Output helper functions

**Chuẩn bị cho Day 11:**
- Ôn lại function basics và scope
- Thực hành viết functions cho thuật toán
- Làm xong bài tập về nhà
- Chuẩn bị học Lambda functions và Recursion