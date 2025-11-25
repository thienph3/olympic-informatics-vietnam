# Day 5: Vòng lặp while và break/continue

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Vòng lặp while cơ bản (45')

### 📚 Lý thuyết (15')

#### Cú pháp vòng lặp while
```python
# Cú pháp cơ bản
while điều_kiện:
    # Khối lệnh lặp
    lệnh1
    lệnh2
    # Cần có lệnh thay đổi điều kiện để tránh vô hạn
```

#### So sánh for và while
```python
# For loop - biết trước số lần lặp
for i in range(5):
    print(i)

# While loop - lặp đến khi điều kiện sai
i = 0
while i < 5:
    print(i)
    i += 1  # Quan trọng: phải thay đổi biến điều kiện
```

#### Ứng dụng while
```python
# 1. Nhập dữ liệu đến khi hợp lệ
age = -1
while age < 0 or age > 150:
    age = int(input("Nhập tuổi (0-150): "))
    if age < 0 or age > 150:
        print("Tuổi không hợp lệ!")

# 2. Xử lý số học
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count

# 3. Tìm kiếm
def find_first_divisible(start, divisor):
    current = start
    while current % divisor != 0:
        current += 1
    return current
```

#### Vòng lặp vô hạn và cách tránh
```python
# VÔ HẠN - Tránh!
# while True:
#     print("Vô hạn")

# Đúng cách
count = 0
while True:
    print(f"Lần {count}")
    count += 1
    if count >= 5:  # Điều kiện thoát
        break

# Hoặc
count = 0
while count < 5:
    print(f"Lần {count}")
    count += 1
```

### 💻 Thực hành (30')

#### Bài tập 1: Validation input với while

**Yêu cầu:** Sử dụng vòng lặp while để validation input: nhập số trong khoảng, kiểm tra mật khẩu mạnh.

**File thực hành:** [problem050101.py](problem050101.py)

#### Bài tập 2: Xử lý số học với while

**Yêu cầu:** Sử dụng while để đảo ngược số, kiểm tra palindrome, tính tổng chữ số, GCD và dãy Fibonacci.

**File thực hành:** [problem050102.py](problem050102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Break và continue (45')

### 📚 Lý thuyết (20')

#### Lệnh break
```python
# Break thoát khỏi vòng lặp ngay lập tức
for i in range(10):
    if i == 5:
        break  # Thoát khi i = 5
    print(i)  # In: 0, 1, 2, 3, 4

# Break trong while
count = 0
while True:
    print(count)
    count += 1
    if count >= 3:
        break  # Thoát vòng lặp vô hạn
```

#### Lệnh continue
```python
# Continue bỏ qua phần còn lại của lần lặp hiện tại
for i in range(10):
    if i % 2 == 0:
        continue  # Bỏ qua số chẵn
    print(i)  # In: 1, 3, 5, 7, 9

# Continue trong while
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)  # In: 1, 3, 5, 7, 9
```

#### Break và continue trong nested loops
```python
# Break chỉ thoát vòng lặp trong cùng
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            break  # Chỉ thoát vòng for j
        print(f"  Inner loop: {j}")
    print("  After inner loop")

# Sử dụng flag để thoát tất cả vòng lặp
found = False
for i in range(3):
    if found:
        break
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
        print(f"({i}, {j})")
```

#### Else với vòng lặp
```python
# Else chỉ chạy khi vòng lặp kết thúc bình thường (không break)
for i in range(5):
    if i == 10:  # Điều kiện không bao giờ đúng
        break
    print(i)
else:
    print("Vòng lặp hoàn thành bình thường")

# Ví dụ thực tế: tìm kiếm
numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"Tìm thấy {target}")
        break
else:
    print(f"Không tìm thấy {target}")
```

### 💻 Thực hành (25')

#### Bài tập 1: Tìm kiếm với break/continue

**Yêu cầu:** Sử dụng break/continue để tìm số nguyên tố, tìm ước số và tìm phần tử thỏa điều kiện.

**File thực hành:** [problem050201.py](problem050201.py)

#### Bài tập 2: Game với break/continue

**Yêu cầu:** Tạo game đoán số sử dụng break/continue để điều khiển luồng game và validation input.

**File thực hành:** [problem050202.py](problem050202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Else trong vòng lặp (45')

### 📚 Lý thuyết (15')

#### Else với for loop
```python
# Else chạy khi for loop hoàn thành bình thường (không break)
for i in range(5):
    print(i)
else:
    print("For loop hoàn thành")

# Else không chạy khi có break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Không in ra vì có break")
```

#### Else với while loop
```python
# Else với while
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop hoàn thành")

# Else không chạy khi có break
count = 0
while count < 10:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("Không in ra vì có break")
```

#### Ứng dụng thực tế của else
```python
# Tìm kiếm phần tử
def search_element(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    else:
        return -1  # Không tìm thấy

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True  # Không tìm thấy ước nào

# Validation input
def get_positive_number():
    while True:
        try:
            num = float(input("Nhập số dương: "))
            if num > 0:
                return num
            print("Số phải dương!")
        except ValueError:
            print("Vui lòng nhập số!")
    else:
        print("Không bao giờ chạy vì while True")
```

### 💻 Thực hành (30')

#### Bài tập 1: Tìm kiếm với else

**Yêu cầu:** Sử dụng else với vòng lặp để tìm kiếm, kiểm tra số nguyên tố và validation input.

**File thực hành:** [problem050301.py](problem050301.py)



---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Ứng dụng while trong Olympic (45')

### 📚 Lý thuyết (15')

#### Thuật toán Euclidean (GCD)
```python
def gcd_euclidean(a, b):
    """Thuật toán Euclidean tìm ước chung lớn nhất"""
    while b != 0:
        print(f"gcd({a}, {b})")
        a, b = b, a % b
    return a

def lcm(a, b):
    """Bội chung nhỏ nhất"""
    return abs(a * b) // gcd_euclidean(a, b)
```

#### Thuật toán số học
```python
# Kiểm tra số hoàn hảo
def is_perfect_number(n):
    if n <= 1:
        return False
    
    divisor_sum = 1  # 1 luôn là ước
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Tránh đếm trùng với số chính phương
                divisor_sum += n // i
        i += 1
    
    return divisor_sum == n

# Phân tích thừa số nguyên tố
def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
```

#### Xử lý chuỗi và số
```python
# Chuyển đổi hệ số
def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    i = len(binary_str) - 1
    
    while i >= 0:
        if binary_str[i] == '1':
            decimal += 2 ** power
        power += 1
        i -= 1
    
    return decimal
```

### 💻 Thực hành (30')

#### Bài tập 1: Thuật toán số học Olympic

**Yêu cầu:** Sử dụng while trong thuật toán Euclidean mở rộng, tìm số Armstrong và số nguyên tố.

**File thực hành:** [problem050401.py](problem050401.py)

#### Bài tập 2: Chuyển đổi hệ số và xử lý bit

**Yêu cầu:** Sử dụng while để chuyển đổi hệ số, thao tác bit và thuật toán Gray Code.

**File thực hành:** [problem050402.py](problem050402.py)

---

## Bài tập về nhà

### Bài 1: Thuật toán Collatz Conjecture
Viết chương trình kiểm tra giả thuyết Collatz:
- Nếu n chẵn: n = n/2
- Nếu n lẻ: n = 3n + 1
- Lặp đến khi n = 1
- Đếm số bước và tìm giá trị lớn nhất trong quá trình
- Test với nhiều số khác nhau

### Bài 2: Máy tính phân số
Tạo máy tính phân số với while loop:
- Menu: cộng, trừ, nhân, chia phân số
- Nhập phân số dạng a/b
- Rút gọn kết quả (dùng GCD)
- Validation input (mẫu số khác 0)
- Chơi đến khi người dùng chọn thoát

### Bài 3: Game "Bulls and Cows"
Tạo game đoán số 4 chữ số:
- Máy tạo số bí mật 4 chữ số không trùng
- Người chơi đoán, máy trả về:
  - Bulls: số chữ số đúng vị trí
  - Cows: số chữ số đúng nhưng sai vị trí
- Chơi đến khi đoán đúng
- Đếm số lần đoán và cho điểm

### Gợi ý làm bài
1. Sử dụng while với điều kiện dừng rõ ràng
2. Kết hợp break/continue cho logic phức tạp
3. Sử dụng else để xử lý trường hợp không tìm thấy
4. Validation input kỹ lưỡng với try-except

---

## Tổng kết Day 5

**Đã học:**
- Vòng lặp while: cú pháp và ứng dụng
- Break và continue: điều khiển luồng vòng lặp
- Else với vòng lặp: xử lý khi hoàn thành bình thường
- Validation input với while
- Thuật toán số học: GCD, số Armstrong, số nguyên tố
- Chuyển đổi hệ số và thao tác bit
- Ứng dụng while trong bài toán Olympic

**Chuẩn bị cho Day 6:**
- Ôn lại break/continue và else
- Thực hành thuật toán với while
- Làm xong bài tập về nhà
- Chuẩn bị học pattern printing nâng cao