# Day 13: Tìm kiếm tuyến tính, binary search cơ bản

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Tìm kiếm tuyến tính (Linear Search) (45')

### 📚 Lý thuyết (15')

#### Khái niệm tìm kiếm tuyến tính
```python
# Tìm kiếm tuyến tính cơ bản
def linear_search(arr, target):
    """
    Tìm kiếm phần tử trong mảng theo thứ tự từ đầu đến cuối
    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Trả về index của phần tử
    return -1  # Không tìm thấy

# Ví dụ sử dụng
numbers = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(numbers, target)
print(f"Phần tử {target} ở vị trí: {result}")
```

#### Các biến thể của linear search
```python
# Tìm tất cả vị trí xuất hiện
def linear_search_all(arr, target):
    """Tìm tất cả vị trí của target trong mảng"""
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions

# Tìm kiếm với điều kiện
def linear_search_condition(arr, condition):
    """Tìm phần tử đầu tiên thỏa mãn điều kiện"""
    for i in range(len(arr)):
        if condition(arr[i]):
            return i
    return -1

# Ví dụ: tìm số chẵn đầu tiên
numbers = [1, 3, 5, 8, 9, 12]
even_pos = linear_search_condition(numbers, lambda x: x % 2 == 0)
print(f"Số chẵn đầu tiên ở vị trí: {even_pos}")

# Tìm kiếm trong string
def search_substring(text, pattern):
    """Tìm vị trí đầu tiên của pattern trong text"""
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

text = "hello world programming"
pattern = "world"
pos = search_substring(text, pattern)
print(f"Pattern '{pattern}' ở vị trí: {pos}")
```

#### Tối ưu hóa linear search
```python
# Sentinel search - thêm phần tử canh gác
def sentinel_search(arr, target):
    """
    Tối ưu linear search bằng cách thêm sentinel
    Giảm số lần kiểm tra điều kiện trong loop
    """
    n = len(arr)
    last = arr[n-1]  # Lưu phần tử cuối
    arr[n-1] = target  # Đặt sentinel
    
    i = 0
    while arr[i] != target:
        i += 1
    
    arr[n-1] = last  # Khôi phục phần tử cuối
    
    if i < n-1 or arr[n-1] == target:
        return i
    return -1

# Jump search - nhảy theo bước
import math

def jump_search(arr, target):
    """
    Tìm kiếm nhảy bước để giảm số phép so sánh
    Time complexity: O(√n)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Tìm block chứa target
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search trong block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    return -1
```

### 💻 Thực hành (30')

#### Bài tập 1: Linear search cơ bản và biến thể

**Yêu cầu:** Implement các thuật toán linear search và biến thể.

**File thực hành:** [problem130101.py](problem130101.py)

#### Bài tập 2: Ứng dụng linear search trong Olympic

**Yêu cầu:** Giải các bài toán Olympic sử dụng linear search.

**File thực hành:** [problem130102.py](problem130102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Binary Search cơ bản (45')

### 📚 Lý thuyết (20')

#### Khái niệm Binary Search
```python
# Binary search cơ bản (iterative)
def binary_search(arr, target):
    """
    Tìm kiếm nhị phân trong mảng đã sắp xếp
    Time complexity: O(log n)
    Space complexity: O(1)
    """
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

# Binary search recursive
def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary search đệ quy
    Space complexity: O(log n) do call stack
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Ví dụ sử dụng
sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(sorted_arr, target)
print(f"Phần tử {target} ở vị trí: {result}")
```

#### Tìm vị trí chèn (Insert position)
```python
def search_insert_position(arr, target):
    """
    Tìm vị trí để chèn target vào mảng sắp xếp
    Trả về index nhỏ nhất i sao cho arr[i] >= target
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Ví dụ
arr = [1, 3, 5, 6]
target = 5
pos = search_insert_position(arr, target)
print(f"Vị trí chèn {target}: {pos}")

target = 2
pos = search_insert_position(arr, target)
print(f"Vị trí chèn {target}: {pos}")
```

#### Tìm first và last occurrence
```python
def find_first_occurrence(arr, target):
    """Tìm vị trí đầu tiên của target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Tiếp tục tìm bên trái
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_last_occurrence(arr, target):
    """Tìm vị trí cuối cùng của target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Tiếp tục tìm bên phải
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_range(arr, target):
    """Tìm range [first, last] của target"""
    first = find_first_occurrence(arr, target)
    if first == -1:
        return [-1, -1]
    last = find_last_occurrence(arr, target)
    return [first, last]

# Ví dụ
arr = [5, 7, 7, 8, 8, 8, 10]
target = 8
range_result = find_range(arr, target)
print(f"Range của {target}: {range_result}")
```

#### Binary search trên answer space
```python
def sqrt_binary_search(x):
    """
    Tìm căn bậc hai nguyên của x bằng binary search
    Tìm số nguyên lớn nhất k sao cho k*k <= x
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # right là giá trị lớn nhất thỏa mãn

# Ví dụ
x = 8
result = sqrt_binary_search(x)
print(f"Căn bậc hai nguyên của {x}: {result}")
```

### 💻 Thực hành (25')

#### Bài tập 1: Binary search implementations

**Yêu cầu:** Implement binary search và các biến thể.

**File thực hành:** [problem130201.py](problem130201.py)

#### Bài tập 2: Binary search applications

**Yêu cầu:** Ứng dụng binary search trong các bài toán thực tế.

**File thực hành:** [problem130202.py](problem130202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: So sánh và phân tích thuật toán (45')

### 📚 Lý thuyết (15')

#### So sánh Linear vs Binary Search
```python
import time
import random

def compare_search_algorithms():
    """So sánh hiệu suất Linear vs Binary Search"""
    
    # Tạo dữ liệu test
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        # Tạo mảng sắp xếp
        arr = list(range(size))
        target = random.randint(0, size-1)
        
        print(f"\nKích thước mảng: {size:,}")
        
        # Test Linear Search
        start = time.time()
        linear_result = linear_search(arr, target)
        linear_time = time.time() - start
        
        # Test Binary Search
        start = time.time()
        binary_result = binary_search(arr, target)
        binary_time = time.time() - start
        
        print(f"Linear Search: {linear_time:.6f}s")
        print(f"Binary Search: {binary_time:.6f}s")
        print(f"Tỷ lệ: {linear_time/binary_time:.2f}x")

# Phân tích độ phức tạp
def analyze_complexity():
    """Phân tích độ phức tạp thời gian"""
    
    print("Độ phức tạp thời gian:")
    print("Linear Search:")
    print("  - Best case: O(1) - phần tử đầu tiên")
    print("  - Average case: O(n/2) = O(n)")
    print("  - Worst case: O(n) - phần tử cuối hoặc không có")
    
    print("\nBinary Search:")
    print("  - Best case: O(1) - phần tử ở giữa")
    print("  - Average case: O(log n)")
    print("  - Worst case: O(log n)")
    
    print("\nĐộ phức tạp không gian:")
    print("Linear Search: O(1)")
    print("Binary Search (iterative): O(1)")
    print("Binary Search (recursive): O(log n)")
```

#### Khi nào sử dụng thuật toán nào
```python
def choose_search_algorithm(data_size, is_sorted, search_frequency):
    """
    Hướng dẫn chọn thuật toán tìm kiếm
    
    Args:
        data_size: Kích thước dữ liệu
        is_sorted: Dữ liệu đã sắp xếp chưa
        search_frequency: Tần suất tìm kiếm (low/medium/high)
    """
    
    if not is_sorted:
        if search_frequency == "low":
            return "Linear Search - không cần sắp xếp"
        elif data_size < 1000:
            return "Linear Search - dữ liệu nhỏ"
        else:
            return "Sắp xếp trước + Binary Search"
    
    else:  # Dữ liệu đã sắp xếp
        if data_size < 100:
            return "Linear Search - overhead của Binary Search không đáng kể"
        else:
            return "Binary Search - hiệu quả với dữ liệu lớn"

# Ví dụ sử dụng
scenarios = [
    (100, False, "low"),
    (10000, False, "high"),
    (1000000, True, "medium"),
    (50, True, "high")
]

for size, sorted_flag, freq in scenarios:
    recommendation = choose_search_algorithm(size, sorted_flag, freq)
    print(f"Size: {size}, Sorted: {sorted_flag}, Frequency: {freq}")
    print(f"Recommendation: {recommendation}\n")
```

### 💻 Thực hành (30')

#### Bài tập 1: Performance analysis

**Yêu cầu:** So sánh hiệu suất các thuật toán tìm kiếm.

**File thực hành:** [problem130301.py](problem130301.py)

#### Bài tập 2: Algorithm selection

**Yêu cầu:** Chọn thuật toán phù hợp cho các tình huống khác nhau.

**File thực hành:** [problem130302.py](problem130302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Ứng dụng trong Olympic (45')

### 📚 Lý thuyết (15')

#### Bài toán Olympic điển hình
```python
# Bài toán 1: Tìm cặp số có tổng bằng target
def two_sum_sorted(arr, target):
    """
    Tìm cặp số trong mảng sắp xếp có tổng = target
    Sử dụng two pointers technique
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

# Bài toán 2: Tìm peak element
def find_peak_element(arr):
    """
    Tìm peak element (phần tử lớn hơn các phần tử kề bên)
    Sử dụng binary search
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Bài toán 3: Search in rotated sorted array
def search_rotated_array(arr, target):
    """
    Tìm kiếm trong mảng sắp xếp bị xoay
    Ví dụ: [4,5,6,7,0,1,2] là [0,1,2,4,5,6,7] bị xoay
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Kiểm tra nửa nào được sắp xếp
        if arr[left] <= arr[mid]:  # Nửa trái được sắp xếp
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Nửa phải được sắp xếp
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

#### Kỹ thuật tối ưu hóa
```python
# Technique 1: Binary search on answer
def minimum_days_to_make_bouquets(bloomDay, m, k):
    """
    Tìm số ngày tối thiểu để làm m bó hoa,
    mỗi bó cần k bông liền kề
    """
    def can_make_bouquets(days):
        bouquets = 0
        consecutive = 0
        
        for bloom in bloomDay:
            if bloom <= days:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0
        
        return bouquets >= m
    
    if len(bloomDay) < m * k:
        return -1
    
    left, right = min(bloomDay), max(bloomDay)
    
    while left < right:
        mid = (left + right) // 2
        if can_make_bouquets(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Technique 2: Binary search với floating point
def find_square_root(x, precision=1e-6):
    """
    Tìm căn bậc hai với độ chính xác cho trước
    """
    if x < 0:
        return None
    if x < 1:
        left, right = 0, 1
    else:
        left, right = 0, x
    
    while right - left > precision:
        mid = (left + right) / 2
        if mid * mid > x:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2
```

### 💻 Thực hành (30')

#### Bài tập 1: Olympic search problems

**Yêu cầu:** Giải các bài toán Olympic sử dụng search algorithms.

**File thực hành:** [problem130401.py](problem130401.py)

#### Bài tập 2: Advanced search techniques

**Yêu cầu:** Implement advanced search techniques cho Olympic.

**File thực hành:** [problem130402.py](problem130402.py)

---

## Bài tập về nhà

### Bài 1: Search Algorithm Library
Tạo thư viện search algorithms:
- Linear search và các biến thể
- Binary search và applications
- Specialized search algorithms
- Performance benchmarking tools
- Test cases và validation

### Bài 2: Olympic Search Problems
Giải các bài toán Olympic:
- Two sum, three sum problems
- Search in special arrays
- Peak finding problems
- Range query problems
- Optimization problems using binary search

### Bài 3: Search Visualization
Tạo tool visualization:
- Animate search process
- Compare algorithm performance
- Interactive search demo
- Step-by-step execution
- Complexity analysis charts

### Gợi ý làm bài
1. Hiểu rõ điều kiện tiên quyết của từng thuật toán
2. Chú ý edge cases và boundary conditions
3. Optimize cho từng loại input cụ thể
4. Sử dụng appropriate data structures

---

## Tổng kết Day 13

**Đã học:**
- Linear Search: cơ bản, biến thể, tối ưu hóa
- Binary Search: iterative, recursive, applications
- So sánh thuật toán: complexity analysis, selection criteria
- Olympic applications: advanced techniques, problem patterns
- Performance optimization: algorithm selection, implementation tricks

**Kỹ năng đạt được:**
- Implement search algorithms efficiently
- Analyze time/space complexity
- Choose appropriate algorithm for problems
- Solve Olympic-level search problems
- Optimize search performance

**Chuẩn bị Day 14:**
- Ôn tập binary search cơ bản
- Tìm hiểu bisect module trong Python
- Thực hành các biến thể của binary search
- Chuẩn bị cho advanced search techniques