# Day 1: Python Essentials

## Variables và Data Types

### Basic Data Types
```python
# Integer
age = 18
score = 100

# Float
height = 1.75
pi = 3.14159

# String
name = "Nguyen Van A"
school = 'THPT ABC'

# Boolean
is_student = True
passed = False
```

### Variables Assignment
```python
# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0

# Swapping variables
a, b = b, a
```

## Input/Output Operations

### Input từ người dùng
```python
# Đọc string
name = input("Nhập tên: ")

# Đọc số nguyên
n = int(input())

# Đọc số thực
x = float(input())

# Đọc nhiều số trên 1 dòng
a, b = map(int, input().split())

# Đọc list số nguyên
arr = list(map(int, input().split()))
```

### Output ra màn hình
```python
# Print cơ bản
print("Hello World")
print(42)

# Print với format
name = "An"
age = 18
print(f"Tên: {name}, Tuổi: {age}")

# Print không xuống dòng
print("Hello", end=" ")
print("World")  # Output: Hello World

# Print với separator
print(1, 2, 3, sep="-")  # Output: 1-2-3
```

## Basic Operations

### Arithmetic Operations
```python
a, b = 10, 3

# Các phép toán cơ bản
print(a + b)    # 13 (cộng)
print(a - b)    # 7 (trừ)
print(a * b)    # 30 (nhân)
print(a / b)    # 3.333... (chia thực)
print(a // b)   # 3 (chia nguyên)
print(a % b)    # 1 (chia lấy dư)
print(a ** b)   # 1000 (lũy thừa)
```

### Comparison Operations
```python
a, b = 5, 3

print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False
print(a == b)   # False
print(a != b)   # True
```

### Logical Operations
```python
x, y = True, False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

## Lists (Danh sách)

### Tạo và truy cập list
```python
# Tạo list
numbers = [1, 2, 3, 4, 5]
names = ["An", "Binh", "Chi"]
mixed = [1, "hello", 3.14, True]

# Truy cập phần tử
print(numbers[0])    # 1 (phần tử đầu)
print(numbers[-1])   # 5 (phần tử cuối)
print(numbers[1:4])  # [2, 3, 4] (slice)
```

### Thao tác với list
```python
arr = [1, 2, 3]

# Thêm phần tử
arr.append(4)        # [1, 2, 3, 4]
arr.insert(0, 0)     # [0, 1, 2, 3, 4]

# Xóa phần tử
arr.remove(2)        # Xóa giá trị 2
del arr[0]           # Xóa phần tử tại index 0
popped = arr.pop()   # Xóa và trả về phần tử cuối

# Độ dài list
print(len(arr))
```

## Ví dụ thực tế

### Bài 1: Tính tổng 2 số
```python
a = int(input())
b = int(input())
print(a + b)
```

### Bài 2: Tìm max trong list
```python
n = int(input())
arr = list(map(int, input().split()))
print(max(arr))
```

### Bài 3: Đếm số chẵn
```python
n = int(input())
arr = list(map(int, input().split()))
count = 0
for x in arr:
    if x % 2 == 0:
        count += 1
print(count)
```

## Control Structures Cơ bản

### Conditions (if/elif/else)
```python
# If cơ bản
age = int(input())
if age >= 18:
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")

# If-elif-else
score = int(input())
if score >= 90:
    print("Giỏi")
elif score >= 70:
    print("Khá")
elif score >= 50:
    print("Trung bình")
else:
    print("Yếu")
```

### Loops (Vòng lặp)
```python
# For loop với range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# For loop với list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
```

### Nested Loops
```python
# Vòng lặp lồng nhau
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

## Lưu ý quan trọng

1. **Indexing**: Python bắt đầu từ index 0
2. **Indentation**: Sử dụng 4 spaces cho mỗi level - Rất quan trọng!
3. **Case sensitive**: `Name` khác `name`
4. **Dynamic typing**: Không cần khai báo kiểu dữ liệu
5. **Modulo operator**: `%` dùng để lấy số dư (rất hữu ích trong Olympic)