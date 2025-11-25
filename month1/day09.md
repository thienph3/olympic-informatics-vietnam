# Day 9: Tuple và String methods

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Tuple cơ bản (45')

### 📚 Lý thuyết (15')

#### Khái niệm Tuple
```python
# Tuple là cấu trúc dữ liệu có thứ tự, KHÔNG thể thay đổi (immutable)
# Tạo tuple
empty_tuple = ()
single_tuple = (5,)  # Chú ý dấu phẩy
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Không cần dấu ngoặc
coordinates = 10, 20
point = 1, 2, 3

print(type(coordinates))  # <class 'tuple'>
```

#### Truy cập và indexing
```python
point = (10, 20, 30)

# Indexing giống list
print(point[0])   # 10
print(point[-1])  # 30

# Slicing
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[1:4])   # (2, 3, 4)
print(numbers[:3])    # (1, 2, 3)
print(numbers[::2])   # (1, 3, 5)

# Không thể thay đổi
# point[0] = 100  # TypeError!
```

#### Tuple unpacking
```python
# Unpacking cơ bản
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")

# Unpacking với nhiều giá trị
person = ("Alice", 25, "Engineer")
name, age, job = person

# Swapping variables
a, b = 1, 2
a, b = b, a  # Hoán đổi
print(f"a = {a}, b = {b}")

# Unpacking với *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"first: {first}, middle: {middle}, last: {last}")
```

#### Tuple methods và operations
```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - đếm số lần xuất hiện
print(numbers.count(2))  # 3

# index() - tìm vị trí đầu tiên
print(numbers.index(3))  # 2

# len() - độ dài
print(len(numbers))  # 7

# in/not in - kiểm tra tồn tại
print(2 in numbers)      # True
print(10 not in numbers) # True

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)
```

### 💻 Thực hành (30')

#### Bài tập 1: Tuple cơ bản và unpacking

**Yêu cầu:** Tạo tuple, truy cập phần tử, unpacking và hoán đổi biến.

**File thực hành:** [problem090101.py](problem090101.py)

#### Bài tập 2: Xử lý tọa độ và điểm

**Yêu cầu:** Sử dụng tuple để biểu diễn tọa độ, tính khoảng cách và xử lý hình học.

**File thực hành:** [problem090102.py](problem090102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: String methods cơ bản (45')

### 📚 Lý thuyết (20')

#### String formatting và case methods
```python
text = "Hello World"

# Case methods
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.capitalize()) # Hello world
print(text.title())      # Hello World
print(text.swapcase())   # hELLO wORLD

# Check case
print(text.isupper())    # False
print(text.islower())    # False
print(text.istitle())    # True

# Strip methods
text = "  Hello World  "
print(text.strip())      # "Hello World"
print(text.lstrip())     # "Hello World  "
print(text.rstrip())     # "  Hello World"
print(text.strip("H "))  # "ello World"
```

#### String search và replace
```python
text = "Python is awesome. Python is powerful."

# Find methods
print(text.find("Python"))     # 0 (vị trí đầu tiên)
print(text.rfind("Python"))    # 19 (vị trí cuối cùng)
print(text.find("Java"))       # -1 (không tìm thấy)

# Index methods (giống find nhưng raise exception nếu không tìm thấy)
print(text.index("Python"))    # 0

# Count occurrences
print(text.count("Python"))    # 2
print(text.count("is"))        # 2

# Replace
new_text = text.replace("Python", "Java")
print(new_text)  # "Java is awesome. Java is powerful."

# Replace với limit
limited = text.replace("Python", "Java", 1)  # Chỉ thay thế lần đầu
print(limited)   # "Java is awesome. Python is powerful."
```

#### String validation methods
```python
# Check content type
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True
print("   ".isspace())      # True

# Check string properties
print("Hello World".startswith("Hello"))  # True
print("Hello World".endswith("World"))    # True
print("Hello World".startswith(("Hi", "Hello")))  # True

# Other checks
print("hello world".islower())  # True
print("HELLO WORLD".isupper())  # True
print("Hello World".istitle())  # True
```

#### String split và join
```python
# Split methods
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# Split với limit
limited_split = text.split(",", 1)
print(limited_split)  # ['apple', 'banana,cherry']

# Split lines
multiline = "line1\nline2\nline3"
lines = multiline.splitlines()
print(lines)  # ['line1', 'line2', 'line3']

# Join method
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # "Python is awesome"

# Join với separator khác
csv_line = ",".join(["apple", "banana", "cherry"])
print(csv_line)  # "apple,banana,cherry"
```

### 💻 Thực hành (25')

#### Bài tập 1: String methods cơ bản

**Yêu cầu:** Thực hành các string methods: case, strip, find, replace, validation.

**File thực hành:** [problem090201.py](problem090201.py)

#### Bài tập 2: Xử lý văn bản và parsing

**Yêu cầu:** Sử dụng string methods để xử lý văn bản, parse dữ liệu và format output.

**File thực hành:** [problem090202.py](problem090202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: String formatting nâng cao (45')

### 📚 Lý thuyết (15')

#### f-strings (Python 3.6+)
```python
name = "Alice"
age = 25
score = 95.67

# f-string cơ bản
print(f"Hello, {name}!")
print(f"{name} is {age} years old")

# Formatting numbers
print(f"Score: {score:.2f}")      # 95.67
print(f"Score: {score:.1f}")      # 95.7
print(f"Age: {age:03d}")          # 025

# Expressions trong f-string
print(f"Next year: {age + 1}")
print(f"Name length: {len(name)}")
print(f"Uppercase: {name.upper()}")

# Alignment
print(f"'{name:>10}'")   # Right align
print(f"'{name:<10}'")   # Left align  
print(f"'{name:^10}'")   # Center align
```

#### format() method
```python
# Positional arguments
template = "Hello, {}! You are {} years old."
print(template.format("Bob", 30))

# Named arguments
template = "Hello, {name}! You are {age} years old."
print(template.format(name="Charlie", age=35))

# Mixed arguments
template = "Hello, {0}! You are {age} years old and live in {0}."
print(template.format("David", age=40))

# Format specifications
print("Score: {:.2f}".format(87.6789))
print("Number: {:05d}".format(42))
print("Percentage: {:.1%}".format(0.856))
```

#### % formatting (old style)
```python
name = "Eve"
age = 28
score = 92.5

# Basic formatting
print("Hello, %s!" % name)
print("%s is %d years old" % (name, age))
print("Score: %.2f" % score)

# Dictionary formatting
data = {"name": "Frank", "age": 33}
print("Hello, %(name)s! Age: %(age)d" % data)
```

### 💻 Thực hành (30')

#### Bài tập 1: String formatting techniques

**Yêu cầu:** Thực hành f-strings, format(), % formatting với các kiểu dữ liệu khác nhau.

**File thực hành:** [problem090301.py](problem090301.py)

#### Bài tập 2: Template và report generation

**Yêu cầu:** Tạo templates và generate reports sử dụng string formatting.

**File thực hành:** [problem090302.py](problem090302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Ứng dụng trong Olympic (45')

### 📚 Lý thuyết (15')

#### String algorithms
```python
# Palindrome check
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Anagram check
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# String matching (naive)
def naive_string_match(text, pattern):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions

# Longest common prefix
def longest_common_prefix(strs):
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

#### Text processing for competitive programming
```python
# Parse input efficiently
def parse_multiple_integers(line):
    return list(map(int, line.split()))

def parse_coordinates(line):
    return tuple(map(int, line.split()))

# Generate output format
def format_result(result_list):
    return ' '.join(map(str, result_list))

# Caesar cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result
```

#### Tuple applications in algorithms
```python
# Coordinate processing
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Sorting with tuples
def sort_by_distance_from_origin(points):
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)

# Multiple return values
def min_max_with_indices(arr):
    min_val = min(arr)
    max_val = max(arr)
    min_idx = arr.index(min_val)
    max_idx = arr.index(max_val)
    return (min_val, min_idx), (max_val, max_idx)
```

### 💻 Thực hành (30')

#### Bài tập 1: String algorithms cho Olympic

**Yêu cầu:** Implement các thuật toán string: palindrome, anagram, pattern matching, cipher.

**File thực hành:** [problem090401.py](problem090401.py)

#### Bài tập 2: Tuple trong thuật toán Olympic

**Yêu cầu:** Sử dụng tuple cho tọa độ, sorting, multiple returns trong bài toán Olympic.

**File thực hành:** [problem090402.py](problem090402.py)

---

## Bài tập về nhà

### Bài 1: Text Analyzer
Viết chương trình phân tích văn bản:
- Đếm số từ, câu, đoạn văn
- Tìm từ xuất hiện nhiều nhất
- Tính độ dài trung bình của từ
- Phân tích tần suất ký tự
- Kiểm tra độ phức tạp văn bản (Flesch Reading Ease)

### Bài 2: Coordinate Geometry
Implement các thuật toán hình học với tuple:
- Tính diện tích tam giác từ 3 điểm
- Kiểm tra 3 điểm thẳng hàng
- Tìm điểm gần nhất với điểm cho trước
- Convex Hull (Graham Scan)
- Kiểm tra điểm trong đa giác

### Bài 3: String Compression
Implement thuật toán nén chuỗi:
- Run-length encoding
- Huffman coding (đơn giản)
- LZ77 compression
- So sánh tỷ lệ nén của các thuật toán

### Gợi ý làm bài
1. Sử dụng string methods để xử lý văn bản hiệu quả
2. Tuple unpacking cho multiple assignments
3. f-strings cho output formatting đẹp
4. Regular expressions cho pattern matching phức tạp

---

## Tổng kết Day 9

**Đã học:**
- Tuple: tạo, truy cập, unpacking, methods
- String methods: case, search, replace, validation, split/join
- String formatting: f-strings, format(), % formatting
- Ứng dụng trong Olympic: string algorithms, coordinate processing
- Text processing và parsing techniques
- Tuple trong thuật toán hình học và sorting

**Chuẩn bị cho Day 10:**
- Ôn lại tuple unpacking và string methods
- Thực hành string algorithms
- Làm xong bài tập về nhà
- Chuẩn bị học Function cơ bản