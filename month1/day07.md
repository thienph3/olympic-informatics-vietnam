# Day 7: List cơ bản - indexing, slicing, methods

**Thời gian:** 195 phút (3h15')

---

## Phần 1: List cơ bản và indexing (45')

### 📚 Lý thuyết (15')

#### Khái niệm List
```python
# List là cấu trúc dữ liệu có thứ tự, có thể thay đổi
# Chứa nhiều phần tử khác kiểu dữ liệu

# Tạo list
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# Độ dài list
print(len(numbers))  # 5
```

#### Indexing - Truy cập phần tử
```python
numbers = [10, 20, 30, 40, 50]

# Index dương (từ trái sang phải)
print(numbers[0])   # 10 (phần tử đầu)
print(numbers[1])   # 20
print(numbers[4])   # 50 (phần tử cuối)

# Index âm (từ phải sang trái)
print(numbers[-1])  # 50 (phần tử cuối)
print(numbers[-2])  # 40
print(numbers[-5])  # 10 (phần tử đầu)

# Thay đổi giá trị
numbers[0] = 100
print(numbers)  # [100, 20, 30, 40, 50]
```

#### Kiểm tra phần tử
```python
numbers = [1, 2, 3, 4, 5]

# Kiểm tra tồn tại
print(3 in numbers)      # True
print(6 in numbers)      # False
print(3 not in numbers)  # False

# Tìm vị trí
print(numbers.index(3))  # 2
# print(numbers.index(6))  # ValueError!

# Đếm số lần xuất hiện
data = [1, 2, 3, 2, 2, 4]
print(data.count(2))     # 3
```

### 💻 Thực hành (30')

#### Bài tập 1: Thao tác cơ bản với list

**Yêu cầu:** Tạo list, truy cập phần tử, thay đổi giá trị và kiểm tra tồn tại.

**File thực hành:** [problem070101.py](problem070101.py)

#### Bài tập 2: Xử lý list số và tìm kiếm

**Yêu cầu:** Nhập list số, tìm min/max, tính tổng/trung bình và tìm kiếm phần tử.

**File thực hành:** [problem070102.py](problem070102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Slicing - cắt list (45')

### 📚 Lý thuyết (20')

#### Cú pháp slicing
```python
# list[start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cắt cơ bản
print(numbers[2:5])    # [2, 3, 4] (từ index 2 đến 4)
print(numbers[:5])     # [0, 1, 2, 3, 4] (từ đầu đến 4)
print(numbers[5:])     # [5, 6, 7, 8, 9] (từ 5 đến cuối)
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (toàn bộ)

# Với step
print(numbers[::2])    # [0, 2, 4, 6, 8] (bước nhảy 2)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (từ index 1, bước 2)
print(numbers[::3])    # [0, 3, 6, 9] (bước nhảy 3)
```

#### Slicing với index âm
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Index âm
print(numbers[-3:])    # [7, 8, 9] (3 phần tử cuối)
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6] (bỏ 3 phần tử cuối)
print(numbers[-5:-2])  # [5, 6, 7] (từ -5 đến -3)

# Đảo ngược
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[8:2:-1]) # [8, 7, 6, 5, 4, 3] (từ 8 về 3, bước -1)
```

#### Slicing để thay đổi list
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Thay đổi một đoạn
numbers[2:5] = [20, 30, 40]
print(numbers)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Chèn phần tử
numbers[2:2] = [100, 200]
print(numbers)  # [0, 1, 100, 200, 20, 30, 40, 5, 6, 7, 8, 9]

# Xóa một đoạn
numbers[2:4] = []
print(numbers)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
```

#### Ứng dụng slicing
```python
# Tách chuỗi thành từ
text = "Python is awesome"
words = text.split()
print(words)  # ['Python', 'is', 'awesome']

# Lấy n phần tử đầu/cuối
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_3 = data[:3]      # [1, 2, 3]
last_3 = data[-3:]     # [8, 9, 10]
middle = data[3:-3]    # [4, 5, 6, 7]

# Chia list thành 2 phần
mid = len(data) // 2
left_half = data[:mid]   # [1, 2, 3, 4, 5]
right_half = data[mid:]  # [6, 7, 8, 9, 10]
```

### 💻 Thực hành (25')

#### Bài tập 1: Slicing cơ bản và nâng cao

**Yêu cầu:** Thực hành các kỹ thuật slicing: cắt đoạn, đảo ngược, lấy phần tử theo bước.

**File thực hành:** [problem070201.py](problem070201.py)

#### Bài tập 2: Ứng dụng slicing trong xử lý dữ liệu

**Yêu cầu:** Sử dụng slicing để xử lý chuỗi, chia list và thao tác dữ liệu.

**File thực hành:** [problem070202.py](problem070202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: List methods - phương thức của list (45')

### 📚 Lý thuyết (15')

#### Thêm phần tử
```python
numbers = [1, 2, 3]

# append() - thêm 1 phần tử vào cuối
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# insert() - chèn phần tử tại vị trí
numbers.insert(1, 10)  # Chèn 10 tại index 1
print(numbers)  # [1, 10, 2, 3, 4]

# extend() - thêm nhiều phần tử
numbers.extend([5, 6, 7])
print(numbers)  # [1, 10, 2, 3, 4, 5, 6, 7]

# Toán tử +
new_list = numbers + [8, 9]
print(new_list)  # [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Xóa phần tử
```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# remove() - xóa phần tử đầu tiên có giá trị
numbers.remove(2)  # Xóa số 2 đầu tiên
print(numbers)  # [1, 3, 2, 4, 2, 5]

# pop() - xóa và trả về phần tử tại vị trí
last = numbers.pop()    # Xóa phần tử cuối
print(last)             # 5
print(numbers)          # [1, 3, 2, 4, 2]

second = numbers.pop(1) # Xóa phần tử tại index 1
print(second)           # 3
print(numbers)          # [1, 2, 4, 2]

# clear() - xóa tất cả
# numbers.clear()
# print(numbers)  # []

# del - xóa theo index hoặc slice
del numbers[0]     # Xóa phần tử đầu
print(numbers)     # [2, 4, 2]
```

#### Sắp xếp và đảo ngược
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sắp xếp tại chỗ
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# sort() với reverse
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - tạo list mới đã sắp xếp
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (không thay đổi)
print(sorted_list)  # [1, 1, 3, 4, 5]

# reverse() - đảo ngược tại chỗ
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

### 💻 Thực hành (30')

#### Bài tập 1: List methods cơ bản

**Yêu cầu:** Thực hành các phương thức thêm, xóa, sắp xếp phần tử trong list.

**File thực hành:** [problem070301.py](problem070301.py)

#### Bài tập 2: Quản lý danh sách học sinh

**Yêu cầu:** Tạo chương trình quản lý danh sách học sinh với các chức năng CRUD.

**File thực hành:** [problem070302.py](problem070302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Ứng dụng list trong Olympic (45')

### 📚 Lý thuyết (15')

#### Thuật toán với list
```python
# Tìm kiếm tuyến tính
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Tìm min/max với vị trí
def find_min_max_with_index(arr):
    if not arr:
        return None, None, None, None
    
    min_val = max_val = arr[0]
    min_idx = max_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    
    return min_val, min_idx, max_val, max_idx

# Loại bỏ phần tử trùng lặp (giữ thứ tự)
def remove_duplicates(arr):
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result
```

#### Xử lý list 2D
```python
# Tạo ma trận
def create_matrix(rows, cols, default_value=0):
    return [[default_value for _ in range(cols)] for _ in range(rows)]

# In ma trận
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:4}", end="")
        print()

# Tính tổng hàng/cột
def sum_rows(matrix):
    return [sum(row) for row in matrix]

def sum_cols(matrix):
    if not matrix:
        return []
    return [sum(matrix[i][j] for i in range(len(matrix))) 
            for j in range(len(matrix[0]))]
```

#### List trong bài toán Olympic
```python
# Sàng Eratosthenes
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(2, n + 1) if is_prime[i]]

# Prefix sum
def prefix_sum(arr):
    result = [0] * len(arr)
    result[0] = arr[0]
    for i in range(1, len(arr)):
        result[i] = result[i-1] + arr[i]
    return result

# Sliding window maximum
def sliding_window_maximum(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        window_max = max(arr[i:i+k])
        result.append(window_max)
    return result
```

### 💻 Thực hành (30')

#### Bài tập 1: Thuật toán cơ bản với list

**Yêu cầu:** Implement các thuật toán tìm kiếm, sắp xếp và xử lý list cơ bản.

**File thực hành:** [problem070401.py](problem070401.py)

#### Bài tập 2: Bài toán Olympic với list

**Yêu cầu:** Giải các bài toán Olympic sử dụng list: sàng số nguyên tố, prefix sum, sliding window.

**File thực hành:** [problem070402.py](problem070402.py)

---

## Bài tập về nhà

### Bài 1: Quản lý điểm số học sinh
Viết chương trình quản lý điểm số:
- Nhập danh sách điểm của học sinh
- Tính điểm trung bình, tìm điểm cao nhất/thấp nhất
- Đếm số học sinh đạt từng loại (Giỏi ≥8, Khá 6.5-8, TB 5-6.5, Yếu <5)
- Sắp xếp danh sách theo điểm giảm dần

### Bài 2: Ma trận xoắn ốc
Tạo ma trận n×n với các số từ 1 đến n² được điền theo hình xoắn ốc:
```
Ví dụ n=4:
 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7
```

### Bài 3: Tìm dãy con có tổng lớn nhất
Cho một list số nguyên (có thể âm), tìm dãy con liên tiếp có tổng lớn nhất:
- Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
- Output: Dãy con [4, -1, 2, 1] có tổng = 6

### Gợi ý làm bài
1. Sử dụng list methods để thao tác dữ liệu
2. Áp dụng slicing cho việc cắt và xử lý đoạn
3. Kết hợp vòng lặp với indexing để duyệt ma trận
4. Sử dụng thuật toán Kadane cho bài 3

---

## Tổng kết Day 7

**Đã học:**
- List cơ bản: tạo, indexing, kiểm tra phần tử
- Slicing: cắt list, đảo ngược, thay đổi đoạn
- List methods: append, insert, remove, pop, sort, reverse
- Ứng dụng list: thuật toán tìm kiếm, ma trận, bài toán Olympic
- Xử lý list 2D và các kỹ thuật tối ưu

**Chuẩn bị cho Day 8:**
- Ôn lại các list methods
- Thực hành slicing và indexing
- Làm xong bài tập về nhà
- Chuẩn bị học list comprehension và nested lists