# Day 2: Advanced Python & Functions

## Advanced Loops và Nested Structures

### Advanced For Loop
```python
# Lặp với start, stop, step
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

# Lặp với index
numbers = [1, 2, 3, 4, 5]
for i, value in enumerate(numbers):
    print(f"Index {i}: {value}")

# Lặp ngược
for i in range(10, 0, -1):
    print(i)
```

### Break và Continue
```python
# Break - thoát khỏi vòng lặp
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue - bỏ qua iteration hiện tại
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9
```

### Nested Loops
```python
# Vòng lặp lồng nhau
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Tạo ma trận
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j)
    matrix.append(row)
print(matrix)
```

## Functions (Hàm)

### Định nghĩa hàm
```python
def greet(name):
    return f"Xin chào {name}!"

def add(a, b):
    return a + b

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Parameters và Arguments
```python
# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 9 (3^2)
print(power(3, 3))  # 27 (3^3)

# Variable arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# Keyword arguments
def student_info(name, age, grade="12"):
    return f"{name}, {age} tuổi, lớp {grade}"

print(student_info("An", 18))
print(student_info(age=17, name="Binh", grade="11"))
```

### Local vs Global variables
```python
x = 10  # Global variable

def test():
    x = 20  # Local variable
    print(f"Local x: {x}")

test()  # Local x: 20
print(f"Global x: {x}")  # Global x: 10

# Sử dụng global keyword
def modify_global():
    global x
    x = 30

modify_global()
print(x)  # 30
```

## List Comprehension cơ bản

### Basic list comprehension
```python
# Tạo list bình phương
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Với điều kiện
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform data
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6]
```

## String Operations

### String methods
```python
text = "Hello World Python"

# Case operations
print(text.upper())     # HELLO WORLD PYTHON
print(text.lower())     # hello world python
print(text.title())     # Hello World Python

# Search and replace
print(text.find("World"))      # 6
print(text.replace("World", "Universe"))  # Hello Universe Python

# Split and join
words = text.split()    # ['Hello', 'World', 'Python']
joined = "-".join(words)  # Hello-World-Python

# Check methods
print("123".isdigit())   # True
print("abc".isalpha())   # True
print("abc123".isalnum())  # True
```

## Ví dụ thực tế

### Bài 1: Tính giai thừa
```python
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input())
print(factorial(n))
```

### Bài 2: Kiểm tra số nguyên tố
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if is_prime(n):
    print("Là số nguyên tố")
else:
    print("Không là số nguyên tố")
```

### Bài 3: Tìm UCLN
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(gcd(a, b))
```

### Bài 4: Đảo ngược chuỗi
```python
def reverse_string(s):
    return s[::-1]

# Hoặc dùng loop
def reverse_string_loop(s):
    result = ""
    for char in s:
        result = char + result
    return result

text = input()
print(reverse_string(text))
```

## Best Practices

1. **Tên hàm**: Sử dụng snake_case (vd: `calculate_sum`)
2. **Docstring**: Mô tả chức năng hàm
3. **Single responsibility**: Mỗi hàm chỉ làm 1 việc
4. **Avoid global variables**: Truyền tham số thay vì dùng biến global