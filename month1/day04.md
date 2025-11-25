# Day 4: Vòng lặp for cơ bản

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Vòng lặp for với range() (45')

### 📚 Lý thuyết (15')

#### Cú pháp vòng lặp for

```python
# Cú pháp cơ bản
for biến in iterable:
    # Khối lệnh lặp
    lệnh1
    lệnh2
```

#### Hàm range()

```python
# range(stop) - từ 0 đến stop-1
for i in range(5):
    print(i)  # In: 0, 1, 2, 3, 4

# range(start, stop) - từ start đến stop-1
for i in range(2, 8):
    print(i)  # In: 2, 3, 4, 5, 6, 7

# range(start, stop, step) - với bước nhảy
for i in range(0, 10, 2):
    print(i)  # In: 0, 2, 4, 6, 8

# range ngược
for i in range(10, 0, -1):
    print(i)  # In: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

#### Ứng dụng cơ bản

```python
# Tính tổng từ 1 đến n
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(f"Tổng từ 1 đến {n}: {total}")

# Tính giai thừa
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### 💻 Thực hành (30')

#### Bài tập 1: Tính toán cơ bản với for

**Yêu cầu:** Sử dụng vòng lặp for để tính tổng số chẵn, tổng bình phương, đếm số chia hết cho 3 và tìm số lớn nhất chia hết cho 7.

**File thực hành:** [problem040101.py](problem040101.py)

#### Bài tập 2: Bảng cửu chương

**Yêu cầu:** In bảng cửu chương từ 1 đến 9 theo cả dạng dọc và ngang.

**File thực hành:** [problem040102.py](problem040102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: For với string và list (45')

### 📚 Lý thuyết (20')

#### Duyệt qua string

```python
# Duyệt từng ký tự
text = "Python"
for char in text:
    print(char)  # P, y, t, h, o, n

# Duyệt với index
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

# Đếm ký tự
def count_char(text, target):
    count = 0
    for char in text:
        if char.lower() == target.lower():
            count += 1
    return count

# Kiểm tra palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
```

#### Duyệt qua list

```python
# Duyệt từng phần tử
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Duyệt với index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# Tìm min/max
def find_min_max(lst):
    if not lst:
        return None, None

    min_val = max_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val
```

#### Hàm enumerate()

```python
# enumerate() trả về (index, value)
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate() với start parameter
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Tìm vị trí của phần tử
def find_positions(lst, target):
    positions = []
    for index, value in enumerate(lst):
        if value == target:
            positions.append(index)
    return positions
```

### 💻 Thực hành (25')

#### Bài tập 1: Xử lý chuỗi

**Yêu cầu:** Đếm các loại ký tự, kiểm tra palindrome và đảo ngược chuỗi.

**File thực hành:** [problem040201.py](problem040201.py)

#### Bài tập 2: Xử lý danh sách số

**Yêu cầu:** Nhập danh sách số, tính các thống kê và tìm giá trị min/max cùng vị trí.

**File thực hành:** [problem040202.py](problem040202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Nested for loops (45')

### 📚 Lý thuyết (15')

#### Vòng lặp lồng nhau

```python
# Cú pháp nested for
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # Xuống dòng sau mỗi hàng ngoài

# Kết quả:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

#### Ma trận và bảng 2D

```python
# Tạo ma trận
rows, cols = 3, 4
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix.append(row)

# In ma trận
for i in range(rows):
    for j in range(cols):
        print(f"{matrix[i][j]:3d}", end=" ")
    print()
```

#### Pattern printing

```python
# Tam giác sao
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Tam giác số
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Hình thoi
for i in range(n):
    # In khoảng trắng
    for j in range(n - i - 1):
        print(" ", end="")
    # In sao
    for j in range(2 * i + 1):
        print("*", end="")
    print()
```

### 💻 Thực hành (30')

#### Bài tập 1: Pattern printing nâng cao

**Yêu cầu:** Sử dụng nested for loops để in các pattern: tam giác vuông, tam giác cân, hình thoi, Pascal và pattern số.

**File thực hành:** [problem040301.py](problem040301.py)

#### Bài tập 2: Ma trận và bảng 2D

**Yêu cầu:** Nhập ma trận, tính tổng hàng/cột, tìm min/max và xử lý đường chéo cho ma trận vuông.

**File thực hành:** [problem040302.py](problem040302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Ứng dụng for trong Olympic (45')

### 📚 Lý thuyết (15')

#### Thuật toán tìm kiếm

```python
# Tìm kiếm tuyến tính
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Tìm tất cả vị trí
def find_all_positions(arr, target):
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions

# Tìm phần tử thỏa mãn điều kiện
def find_first_condition(arr, condition):
    for i in range(len(arr)):
        if condition(arr[i]):
            return i, arr[i]
    return -1, None
```

#### Thuật toán số học

```python
# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tìm ước chung lớn nhất (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Phân tích thừa số nguyên tố
def prime_factors(n):
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

#### Xử lý dãy số

```python
# Tìm dãy con tăng dài nhất
def longest_increasing_subsequence_length(arr):
    if not arr:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

# Kiểm tra dãy đối xứng
def is_symmetric_sequence(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            return False
    return True
```

### 💻 Thực hành (30')

#### Bài tập 1: Bài toán số học Olympic

**Yêu cầu:** Sử dụng sàng Eratosthenes tìm số nguyên tố, kiểm tra số hoàn hảo và tìm cặp số có tổng bằng target.

**File thực hành:** [problem040401.py](problem040401.py)

#### Bài tập 2: Xử lý dãy số và pattern

**Yêu cầu:** Phân tích dãy số: kiểm tra tăng/giảm, tìm dãy con tăng dài nhất, peak/valley, chu kỳ và thống kê tần suất.

**File thực hành:** [problem040402.py](problem040402.py)

---

## Bài tập về nhà

### Bài 1: Số Armstrong

Viết chương trình kiểm tra và tìm tất cả số Armstrong từ 1 đến n:

- Số Armstrong: tổng lũy thừa bậc k của các chữ số bằng chính nó
- VD: 153 = 1³ + 5³ + 3³ (k=3 vì có 3 chữ số)
- In ra tất cả số Armstrong và đếm số lượng

### Bài 2: Ma trận xoắn ốc

Tạo ma trận n×n với các số từ 1 đến n² được sắp xếp theo hình xoắn ốc:

```
Ví dụ n=4:
 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7
```

### Bài 3: Game đoán số với gợi ý

Tạo game đoán số nâng cao:

- Máy tính tạo số ngẫu nhiên từ 1-1000
- Người chơi có tối đa 10 lần đoán
- Sau mỗi lần đoán sai, đưa ra gợi ý thông minh
- Tính điểm dựa trên số lần đoán
- Lưu high score

### Gợi ý làm bài

1. Sử dụng nested loops để phân tích từng chữ số (bài 1)
2. Sử dụng 4 vòng for cho 4 hướng xoắn ốc (bài 2)
3. Sử dụng random module và logic phân tích khoảng (bài 3)
4. Chú ý tối ưu hóa thuật toán cho hiệu suất tốt

---

## Tổng kết Day 4

**Đã học:**

- Vòng lặp for với range(): start, stop, step
- Duyệt qua string và list với for
- Hàm enumerate() để lấy index và value
- Nested for loops và pattern printing
- Thao tác ma trận 2D
- Ứng dụng for trong thuật toán Olympic
- Sàng Eratosthenes, số hoàn hảo, phân tích dãy số

**Chuẩn bị cho Day 5:**

- Ôn lại cách sử dụng range()
- Thực hành với nested loops
- Làm xong bài tập về nhà
- Chuẩn bị học vòng lặp while
