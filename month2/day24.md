# Day 24: Giải đề Olympic cơ bản + Mock test tháng 2

## Mục tiêu
- Áp dụng kiến thức 2 tháng đầu vào giải đề Olympic thực tế
- Làm quen với format đề thi Olympic Tin học
- Thực hiện Mock test đánh giá năng lực
- Rèn luyện kỹ năng quản lý thời gian trong thi

## Phần 1: Phân tích đề Olympic cơ bản (45 phút)

### 1.1 Cấu trúc đề thi Olympic Tin học
```
Đề thi Olympic Tin học THPT thường có:
- 3-4 bài toán
- Thời gian: 3 tiếng (180 phút)
- Điểm: 100 điểm (mỗi bài 25-30 điểm)
- Input/Output: file hoặc standard I/O
```

### 1.2 Phân loại bài toán Olympic cơ bản
1. **Bài toán cài đặt thuật toán**
   - Tìm kiếm, sắp xếp
   - Xử lý mảng, chuỗi
   - Đệ quy đơn giản

2. **Bài toán tối ưu**
   - Tìm min/max
   - Đếm số lượng
   - Kiểm tra điều kiện

3. **Bài toán mô phỏng**
   - Thực hiện theo yêu cầu
   - Xử lý từng bước

### 1.3 Chiến lược giải đề
```python
# Quy trình giải bài Olympic:
# 1. Đọc đề kỹ (5-10 phút)
# 2. Phân tích input/output
# 3. Tìm thuật toán phù hợp
# 4. Cài đặt và test
# 5. Tối ưu nếu cần
```

## Phần 2: Giải đề Olympic mẫu (45 phút)

### 2.1 Bài 1: Tìm số lớn nhất
**Đề bài:** Cho dãy n số nguyên. Tìm số lớn nhất và vị trí của nó.

**Input:** 
- Dòng 1: n (1 ≤ n ≤ 10^5)
- Dòng 2: n số nguyên a₁, a₂, ..., aₙ

**Output:** Số lớn nhất và vị trí (bắt đầu từ 1)

```python
def solve_max_element():
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_val = arr[0]
    max_pos = 1
    
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_pos = i + 1
    
    print(max_val, max_pos)
```

### 2.2 Bài 2: Đếm số chẵn lẻ
**Đề bài:** Đếm số lượng số chẵn và lẻ trong dãy.

```python
def count_even_odd():
    n = int(input())
    arr = list(map(int, input().split()))
    
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = n - even_count
    
    print(even_count, odd_count)
```

### 2.3 Bài 3: Sắp xếp theo yêu cầu
**Đề bài:** Sắp xếp dãy sao cho số chẵn trước, số lẻ sau.

```python
def sort_even_odd():
    n = int(input())
    arr = list(map(int, input().split()))
    
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 == 1]
    
    result = sorted(evens) + sorted(odds)
    print(*result)
```

## Phần 3: Mock test thực hành (45 phút)

### 3.1 Đề Mock test 1
**Thời gian:** 45 phút
**Số bài:** 3 bài

**Bài A: Tổng ước số**
- Input: Số nguyên n (1 ≤ n ≤ 10^6)
- Output: Tổng các ước số của n

**Bài B: Dãy tăng dần**
- Input: Dãy n số
- Output: Độ dài dãy con tăng dần dài nhất

**Bài C: Ma trận xoắn ốc**
- Input: Số n
- Output: Ma trận xoắn ốc n×n

### 3.2 Hướng dẫn làm bài
```python
# Bài A: Tổng ước số
def sum_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

# Bài B: Dãy tăng dần
def longest_increasing_subsequence(arr):
    n = len(arr)
    max_length = 1
    current_length = 1
    
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length
```

## Phần 4: Đánh giá và cải thiện (45 phút)

### 4.1 Tiêu chí đánh giá
1. **Độ chính xác:** Code chạy đúng với test case
2. **Hiệu suất:** Thời gian chạy trong giới hạn
3. **Code style:** Dễ đọc, dễ hiểu
4. **Xử lý edge case:** Trường hợp đặc biệt

### 4.2 Lỗi thường gặp
```python
# Lỗi 1: Không xử lý input đúng format
# Sai:
n = input()  # Chuỗi thay vì số

# Đúng:
n = int(input())

# Lỗi 2: Index out of range
# Sai:
for i in range(n+1):  # Vượt quá độ dài mảng

# Đúng:
for i in range(n):

# Lỗi 3: Không xử lý trường hợp đặc biệt
# Sai:
max_val = arr[0]  # Nếu arr rỗng sẽ lỗi

# Đúng:
if arr:
    max_val = arr[0]
```

### 4.3 Kỹ thuật debug
```python
# 1. In ra giá trị trung gian
def debug_function(arr):
    print(f"Input: {arr}")  # Debug input
    result = process(arr)
    print(f"Output: {result}")  # Debug output
    return result

# 2. Kiểm tra điều kiện
def safe_division(a, b):
    assert b != 0, "Division by zero"
    return a / b

# 3. Test với case đơn giản
def test_function():
    # Test case cơ bản
    assert find_max([1, 2, 3]) == 3
    assert find_max([5, 1, 3]) == 5
    print("All tests passed!")
```

### 4.4 Tối ưu hóa code
```python
# Tối ưu 1: Sử dụng built-in functions
# Chậm:
max_val = arr[0]
for x in arr[1:]:
    if x > max_val:
        max_val = x

# Nhanh:
max_val = max(arr)

# Tối ưu 2: List comprehension
# Chậm:
evens = []
for x in arr:
    if x % 2 == 0:
        evens.append(x)

# Nhanh:
evens = [x for x in arr if x % 2 == 0]

# Tối ưu 3: Sử dụng set cho lookup
# Chậm: O(n)
if x in list_items:  

# Nhanh: O(1)
if x in set_items:
```

## Bài tập thực hành

Hoàn thành 8 bài tập sau để củng cố kiến thức:

1. **problem240101.py**: Giải đề Olympic mẫu - 3 bài cơ bản
2. **problem240102.py**: Mock test 1 - Tổng ước số, dãy tăng, ma trận xoắn ốc
3. **problem240201.py**: Mock test 2 - Số nguyên tố, palindrome, sắp xếp
4. **problem240202.py**: Mock test 3 - Tìm kiếm, đệ quy, xử lý chuỗi
5. **problem240301.py**: Đề thi Olympic 2020 - Bài cơ bản
6. **problem240302.py**: Đề thi Olympic 2021 - Bài dễ
7. **problem240401.py**: Kỹ thuật debug và tối ưu code
8. **problem240402.py**: Chiến lược làm bài thi Olympic

## Tổng kết

Day 24 đánh dấu kết thúc tháng 2 với việc áp dụng toàn bộ kiến thức đã học vào giải đề Olympic thực tế. Học sinh đã:

- Nắm vững Python cơ bản (Tháng 1)
- Hiểu các thuật toán tìm kiếm, sắp xếp (Tháng 2)
- Biết phân tích độ phức tạp và tối ưu code
- Làm quen với format đề thi Olympic
- Rèn luyện kỹ năng làm bài trong thời gian giới hạn

**Chuẩn bị cho Tháng 3:** Cấu trúc dữ liệu nâng cao (collections, heapq, stack, queue, tree)