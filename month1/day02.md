# Day 2: Toán tử và biểu thức

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Toán tử số học (45')

### 📚 Lý thuyết (15')

#### Các toán tử số học cơ bản

**1. Toán tử cơ bản**

```python
# Cộng, trừ, nhân
a = 10 + 5    # 15
b = 10 - 3    # 7
c = 4 * 6     # 24

# Chia thực và chia nguyên
d = 15 / 4    # 3.75 (chia thực)
e = 15 // 4   # 3 (chia nguyên, bỏ phần dư)

# Chia lấy dư
f = 15 % 4    # 3 (15 = 4*3 + 3)

# Lũy thừa
g = 2 ** 3    # 8 (2^3)
h = 5 ** 2    # 25 (5^2)
```

**2. Thứ tự ưu tiên (từ cao đến thấp)**

1. `()` - Ngoặc đơn
2. `**` - Lũy thừa
3. `*`, `/`, `//`, `%` - Nhân, chia
4. `+`, `-` - Cộng, trừ

```python
result = 2 + 3 * 4 ** 2    # 2 + 3 * 16 = 2 + 48 = 50
result2 = (2 + 3) * 4 ** 2 # 5 * 16 = 80
```

**3. Ứng dụng trong Olympic**

- Kiểm tra số chẵn lẻ: `n % 2 == 0`
- Tính chữ số cuối: `n % 10`
- Bỏ chữ số cuối: `n // 10`
- Tính lũy thừa nhanh: `pow(a, b, mod)`

### 💻 Thực hành (30')

#### Bài tập 1: Máy tính nâng cao

**Yêu cầu:** Tạo máy tính có thể thực hiện các phép toán cơ bản với 2 số thực.

**File thực hành:** [problem020101.py](problem020101.py)

#### Bài tập 2: Thao tác với chữ số

**Yêu cầu:** Phân tích các thông tin của một số nguyên (chữ số cuối, bỏ chữ số cuối, chẵn/lẻ, đếm chữ số).

**File thực hành:** [problem020102.py](problem020102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Toán tử so sánh và logic (45')

### 📚 Lý thuyết (20')

#### Toán tử so sánh

```python
a = 10
b = 5

# So sánh bằng
print(a == b)    # False
print(a != b)    # True

# So sánh lớn nhỏ
print(a > b)     # True
print(a < b)     # False
print(a >= b)    # True
print(a <= b)    # False
```

#### Toán tử logic

```python
# AND (và) - cả hai đều True mới True
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# OR (hoặc) - một trong hai True là True
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# NOT (phủ định)
print(not True)         # False
print(not False)        # True
```

#### Kết hợp toán tử

```python
age = 18
score = 85

# Kiểm tra điều kiện phức tạp
is_adult = age >= 18
is_good_student = score >= 80
can_graduate = is_adult and is_good_student

print(f"Đủ tuổi: {is_adult}")
print(f"Học sinh giỏi: {is_good_student}")
print(f"Có thể tốt nghiệp: {can_graduate}")
```

#### Short-circuit evaluation

```python
# Python đánh giá từ trái sang phải và dừng sớm
x = 0
result = (x != 0) and (10 / x > 5)  # Không lỗi vì x != 0 là False
print(result)  # False

# Tương tự với OR
result2 = (x == 0) or (10 / x > 5)  # Không cần tính 10/x
print(result2)  # True
```

### 💻 Thực hành (25')

#### Bài tập 1: Kiểm tra điều kiện

**Yêu cầu:** Nhập thông tin cá nhân và kiểm tra các điều kiện logic (tuổi, BMI, chiều cao).

**File thực hành:** [problem020201.py](problem020201.py)

#### Bài tập 2: Logic game

**Yêu cầu:** Nhập 3 số và kiểm tra các điều kiện logic phức tạp.

**File thực hành:** [problem020202.py](problem020202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Toán tử gán và bitwise (45')

### 📚 Lý thuyết (15')

#### Toán tử gán

```python
# Gán cơ bản
x = 10

# Gán kết hợp với phép toán
x += 5    # x = x + 5 = 15
x -= 3    # x = x - 3 = 12
x *= 2    # x = x * 2 = 24
x /= 4    # x = x / 4 = 6.0
x //= 2   # x = x // 2 = 3.0
x %= 2    # x = x % 2 = 1.0
x **= 3   # x = x ** 3 = 1.0
```

#### Toán tử bitwise (thao tác bit)

```python
# Biểu diễn nhị phân
a = 5     # 101 (nhị phân)
b = 3     # 011 (nhị phân)

# AND bitwise
print(a & b)    # 1 (001)

# OR bitwise
print(a | b)    # 7 (111)

# XOR bitwise
print(a ^ b)    # 6 (110)

# NOT bitwise
print(~a)       # -6

# Dịch bit
print(a << 1)   # 10 (1010) - dịch trái 1 bit
print(a >> 1)   # 2 (10) - dịch phải 1 bit
```

#### Ứng dụng bitwise trong Olympic

```python
# Kiểm tra bit thứ i
def check_bit(n, i):
    return (n >> i) & 1

# Bật bit thứ i
def set_bit(n, i):
    return n | (1 << i)

# Tắt bit thứ i
def clear_bit(n, i):
    return n & ~(1 << i)

# Đếm số bit 1
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

### 💻 Thực hành (30')

#### Bài tập 1: Thao tác gán

**Yêu cầu:** Mô phỏng game với các thao tác gán kết hợp (điểm, mạng, hệ số).

**File thực hành:** [problem020301.py](problem020301.py)

#### Bài tập 2: Thao tác bit

**Yêu cầu:** Thực hiện các thao tác bitwise và phân tích bit của số nguyên.

**File thực hành:** [problem020302.py](problem020302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Math module và ứng dụng (45')

### 📚 Lý thuyết (15')

#### Import math module

```python
import math

# Các hàm toán học cơ bản
print(math.sqrt(16))      # 4.0 - căn bậc hai
print(math.pow(2, 3))     # 8.0 - lũy thừa
print(math.ceil(3.2))     # 4 - làm tròn lên
print(math.floor(3.8))    # 3 - làm tròn xuống
print(math.abs(-5))       # 5 - giá trị tuyệt đối

# Hằng số toán học
print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045

# Hàm lượng giác (radian)
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0
```

#### Hàm hữu ích cho Olympic

```python
import math

# Ước chung lớn nhất
print(math.gcd(12, 18))   # 6

# Giai thừa
print(math.factorial(5))  # 120

# Logarithm
print(math.log(8, 2))     # 3.0 (log cơ số 2)
print(math.log10(1000))   # 3.0 (log cơ số 10)

# Kiểm tra số nguyên tố (cách đơn giản)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

#### Làm tròn số

```python
import math

x = 3.14159

# Các cách làm tròn
print(round(x))           # 3 - làm tròn tự nhiên
print(round(x, 2))        # 3.14 - làm tròn 2 chữ số thập phân
print(math.ceil(x))       # 4 - làm tròn lên
print(math.floor(x))      # 3 - làm tròn xuống
print(math.trunc(x))      # 3 - cắt phần thập phân
```

### 💻 Thực hành (30')

#### Bài tập 1: Máy tính khoa học

**Yêu cầu:** Tạo máy tính sử dụng math module (căn bậc hai, lũy thừa, lượng giác, logarithm).

**File thực hành:** [problem020401.py](problem020401.py)

#### Bài tập 2: Bài toán hình học

**Yêu cầu:** Tính toán hình học (hình tròn, tam giác vuông, hình cầu) sử dụng math module.

**File thực hành:** [problem020402.py](problem020402.py)

#### Bài tập 3: Kiểm tra số nguyên tố

**Yêu cầu:** Viết chương trình kiểm tra số nguyên tố và tìm số nguyên tố trong khoảng.

**File thực hành:** [problem020403.py](problem020403.py)

---

## Bài tập về nhà

### Bài 1: Máy tính phân số

Viết chương trình:

- Nhập hai phân số (tử số và mẫu số)
- Thực hiện các phép toán: +, -, ×, ÷
- Rút gọn kết quả (sử dụng math.gcd)
- Format: "a/b + c/d = e/f"

### Bài 2: Phân tích số

Viết chương trình nhập một số nguyên dương và:

- Đếm số chữ số
- Tính tổng các chữ số
- Tìm chữ số lớn nhất và nhỏ nhất
- Kiểm tra số đối xứng (palindrome)
- Kiểm tra số hoàn hảo

### Bài 3: Bài toán lãi suất

Viết chương trình tính:

- Lãi suất đơn: A = P(1 + rt)
- Lãi suất kép: A = P(1 + r)^t
- So sánh hai loại lãi suất
- Tính thời gian để đạt số tiền mong muốn

### Gợi ý làm bài

1. Sử dụng math.gcd() cho bài 1
2. Sử dụng vòng lặp while và phép % // cho bài 2
3. Sử dụng math.pow() hoặc \*\* cho bài 3
4. Chú ý xử lý trường hợp đặc biệt (chia cho 0, số âm...)

---

## Tổng kết Day 2

**Đã học:**

- Toán tử số học: +, -, \*, /, //, %, \*\*
- Thứ tự ưu tiên của các toán tử
- Toán tử so sánh: ==, !=, <, >, <=, >=
- Toán tử logic: and, or, not
- Toán tử gán: +=, -=, \*=, /=, //=, %=, \*\*=
- Toán tử bitwise: &, |, ^, ~, <<, >>
- Math module: sqrt, pow, ceil, floor, gcd, factorial
- Ứng dụng trong bài toán Olympic

**Chuẩn bị cho Day 3:**

- Ôn lại các toán tử và thứ tự ưu tiên
- Thực hành với math module
- Làm xong bài tập về nhà
