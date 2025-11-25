# Day 1: Giới thiệu Python 3.10 và VSCode

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Setup môi trường (45')

### 📚 Lý thuyết (15')

#### Giới thiệu Python

Python là ngôn ngữ lập trình được tạo ra bởi Guido van Rossum năm 1991. Tên "Python" được đặt theo nhóm hài Monty Python, không phải loài rắn.

**Tại sao chọn Python cho Olympic Tin học?**

- Cú pháp đơn giản, dễ học
- Thư viện chuẩn phong phú (collections, heapq, bisect, itertools)
- Không cần khai báo kiểu dữ liệu
- Xử lý string và list rất mạnh
- Phù hợp với tư duy thuật toán

#### Olympic Tin học THPT

Olympic Tin học THPT là kỳ thi quan trọng nhất về lập trình cho học sinh THPT tại Việt Nam.

**Cấu trúc thi:**

- Thời gian: 3 tiếng
- Số bài: 3-4 bài
- Ngôn ngữ: Pascal, C++, Python
- Môi trường: Thường là Code::Blocks, Dev-C++, hoặc VSCode

**Các cấp thi:**

- Cấp trường → Cấp tỉnh → Cấp quốc gia → Quốc tế (IOI)

#### Lộ trình 6 tháng

**Mục tiêu:** Từ zero đến có thể đạt giải cao Olympic

- **Tháng 1:** Nền tảng Python
- **Tháng 2:** Thuật toán cơ bản + giải đề đơn giản
- **Tháng 3:** Cấu trúc dữ liệu
- **Tháng 4:** Đồ thị và cây + giải đề trung bình
- **Tháng 5:** Thuật toán nâng cao + giải đề khó
- **Tháng 6:** Luyện thi Olympic chuyên sâu

### 💻 Thực hành (30')

#### Bước 1: Cài đặt Python 3.10

1. Truy cập https://python.org
2. Download Python 3.10.x
3. Chạy installer, **QUAN TRỌNG:** Tick "Add Python to PATH"
4. Kiểm tra: Mở Command Prompt, gõ `python --version`

#### Bước 2: Cài đặt VSCode

1. Truy cập https://code.visualstudio.com
2. Download và cài đặt
3. Cài extension "Python" của Microsoft
4. Cài extension "Code Runner" (tùy chọn)

#### Bước 3: Tạo file Python đầu tiên

1. Tạo thư mục `olympic_practice`
2. Mở VSCode, mở thư mục này
3. Tạo file `hello.py`
4. Viết code đầu tiên:

```python
print("Hello, Olympic!")
```

5. Chạy bằng F5 hoặc Ctrl+F5

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Cú pháp cơ bản (45')

### 📚 Lý thuyết (20')

#### Đặc điểm cú pháp Python

**1. Indentation (thụt lề)**
Python sử dụng thụt lề thay vì dấu {} như C++:

```python
# Đúng
if True:
    print("Đây là code bên trong if")
    print("Dòng này cũng bên trong if")
print("Dòng này ở ngoài if")

# Sai - IndentationError
if True:
print("Lỗi thụt lề")
```

**2. Comment (chú thích)**

```python
# Đây là comment một dòng
print("Hello")  # Comment cuối dòng

"""
Đây là comment
nhiều dòng
(docstring)
"""
```

**3. Case sensitive**
Python phân biệt chữ hoa/thường:

```python
name = "Alice"
Name = "Bob"  # Đây là biến khác
NAME = "Charlie"  # Đây cũng là biến khác
```

**4. PEP 8 - Style Guide**

- Tên biến: `snake_case` (vd: `student_name`)
- Tên hằng số: `UPPER_CASE` (vd: `MAX_SIZE`)
- Tên class: `PascalCase` (vd: `StudentInfo`)
- Dòng code không quá 79 ký tự
- 2 dòng trống giữa các function

### 💻 Thực hành (25')

#### Bài tập 1: Hello World nâng cao
**File:** [problem010201.py](problem010201.py)

#### Bài tập 2: Thử nghiệm indentation
**File:** [problem010202.py](problem010202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Biến và kiểu dữ liệu (45')

### 📚 Lý thuyết (15')

#### Biến trong Python

Biến là "nhãn" gắn với một giá trị trong bộ nhớ:

```python
# Khai báo biến (không cần khai báo kiểu)
age = 18
name = "Minh"
height = 1.75
is_student = True
```

#### Các kiểu dữ liệu cơ bản

**1. int (số nguyên)**

```python
positive_num = 42
negative_num = -17
big_num = 123456789012345678901234567890  # Python hỗ trợ số rất lớn
zero = 0
```

**2. float (số thực)**

```python
pi = 3.14159
temperature = -5.5
scientific = 1.23e-4  # 1.23 × 10^(-4)
```

**3. str (chuỗi)**

```python
single_quote = 'Hello'
double_quote = "World"
multiline = """Đây là
chuỗi nhiều dòng"""
empty_string = ""
```

**4. bool (logic)**

```python
is_true = True
is_false = False
# Lưu ý: True/False viết hoa chữ cái đầu
```

#### Hàm kiểm tra kiểu dữ liệu

**type() - Kiểm tra kiểu**

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
```

#### Chuyển đổi kiểu dữ liệu

```python
# Chuyển sang int
int("123")     # 123
int(3.14)      # 3 (cắt phần thập phân)
int(True)      # 1
int(False)     # 0

# Chuyển sang float
float("3.14")  # 3.14
float(42)      # 42.0

# Chuyển sang str
str(123)       # "123"
str(3.14)      # "3.14"

# Chuyển sang bool
bool(1)        # True
bool(0)        # False
bool("")       # False (chuỗi rỗng)
bool("Hello")  # True (chuỗi không rỗng)
```

### 💻 Thực hành (30')

#### Bài tập 1: Khai báo và kiểm tra biến
**File:** [problem010301.py](problem010301.py)

#### Bài tập 2: Chuyển đổi kiểu
**File:** [problem010302.py](problem010302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Input/Output cơ bản (45')

### 📚 Lý thuyết (15')

#### Hàm input()

`input()` luôn trả về string, cần chuyển đổi kiểu nếu cần:

```python
# Nhập chuỗi
name = input("Nhập tên của bạn: ")

# Nhập số (cần chuyển đổi)
age_str = input("Nhập tuổi: ")
age = int(age_str)
# Hoặc viết gọn:
age = int(input("Nhập tuổi: "))
```

#### Hàm print()

**Cú pháp cơ bản:**

```python
print("Hello World")
print("Xin chào", "các bạn")  # In nhiều giá trị
print("Tên:", name, "Tuổi:", age)
```

**Tham số của print():**

```python
# sep: ký tự ngăn cách
print("A", "B", "C", sep="-")  # A-B-C

# end: ký tự kết thúc
print("Hello", end=" ")
print("World")  # Hello World (cùng dòng)

# Mặc định: sep=" ", end="\n"
```

#### Format string

**1. f-string (Python 3.6+, khuyến nghị)**

```python
name = "Alice"
age = 20
print(f"Tôi là {name}, {age} tuổi")
print(f"Năm sau tôi {age + 1} tuổi")
```

**2. .format() method**

```python
print("Tôi là {}, {} tuổi".format(name, age))
print("Tôi là {0}, {1} tuổi".format(name, age))
```

### 💻 Thực hành (30')

#### Bài tập 1: Chương trình chào hỏi
**File:** [problem010401.py](problem010401.py)

#### Bài tập 2: Máy tính đơn giản
**File:** [problem010402.py](problem010402.py)

#### Bài tập 3: Thông tin học sinh
**File:** [problem010403.py](problem010403.py)

---

## Bài tập về nhà

### Bài 1: Chương trình chào hỏi cá nhân

Viết chương trình nhập tên, tuổi của người dùng và in ra lời chào theo format:

```
Xin chào [Tên]!
Bạn [tuổi] tuổi.
Năm sau bạn sẽ [tuổi+1] tuổi.
```

### Bài 2: Tính diện tích hình chữ nhật

Viết chương trình:

- Nhập chiều dài và chiều rộng
- Tính và in ra chu vi, diện tích
- Format: "Hình chữ nhật [dài]×[rộng] có chu vi [chu vi] và diện tích [diện tích]"

### Bài 3: Chuyển đổi nhiệt độ

Viết chương trình chuyển đổi nhiệt độ từ Celsius sang Fahrenheit:

- Công thức: F = C × 9/5 + 32
- Nhập độ C, in ra độ F
- Format: "[C]°C = [F]°F"

### Gợi ý làm bài

1. Tạo file riêng cho mỗi bài (bai1.py, bai2.py, bai3.py)
2. Sử dụng f-string để format output
3. Chú ý chuyển đổi kiểu dữ liệu khi cần
4. Test với nhiều giá trị khác nhau

---

## Tổng kết Day 1

**Đã học:**

- Cài đặt Python 3.10 và VSCode
- Cú pháp cơ bản: indentation, comment, PEP 8
- Kiểu dữ liệu: int, float, str, bool
- Chuyển đổi kiểu dữ liệu
- Input/Output với input() và print()
- Format string với f-string

**Chuẩn bị cho Day 2:**

- Ôn lại các kiểu dữ liệu
- Thực hành thêm với input/output
- Làm xong bài tập về nhà
