# Day 3: Search Algorithms

## Linear Search (Tìm kiếm tuyến tính)

### Khái niệm
Linear search là thuật toán tìm kiếm đơn giản nhất, duyệt qua từng phần tử trong danh sách cho đến khi tìm thấy phần tử cần tìm.

### Implementation
```python
def linear_search(arr, target):
    """
    Tìm kiếm tuyến tính
    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Trả về index
    return -1  # Không tìm thấy

# Ví dụ sử dụng
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(arr, target)
if result != -1:
    print(f"Tìm thấy {target} tại vị trí {result}")
else:
    print(f"Không tìm thấy {target}")
```

### Tìm tất cả vị trí
```python
def linear_search_all(arr, target):
    """Tìm tất cả vị trí xuất hiện của target"""
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions

arr = [1, 3, 2, 3, 5, 3, 7]
target = 3
positions = linear_search_all(arr, target)
print(f"Tìm thấy {target} tại các vị trí: {positions}")  # [1, 3, 5]
```

## Binary Search (Tìm kiếm nhị phân)

### Khái niệm
Binary search chỉ áp dụng được trên mảng đã sắp xếp. Thuật toán chia đôi không gian tìm kiếm ở mỗi bước.

### Implementation (Iterative)
```python
def binary_search(arr, target):
    """
    Tìm kiếm nhị phân (iterative)
    Time complexity: O(log n)
    Space complexity: O(1)
    Yêu cầu: arr phải được sắp xếp
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

# Ví dụ sử dụng
arr = [11, 12, 22, 25, 34, 64, 90]  # Đã sắp xếp
target = 25
result = binary_search(arr, target)
print(f"Tìm thấy {target} tại vị trí {result}")
```

### Implementation (Recursive)
```python
def binary_search_recursive(arr, target, left=0, right=None):
    """Tìm kiếm nhị phân (recursive)"""
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
```

### Tìm vị trí chèn
```python
def binary_search_insert_position(arr, target):
    """
    Tìm vị trí để chèn target vào mảng sắp xếp
    Trả về vị trí nhỏ nhất i sao cho arr[i] >= target
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

arr = [1, 3, 5, 6]
target = 4
pos = binary_search_insert_position(arr, target)
print(f"Chèn {target} tại vị trí {pos}")  # 2
```

## Time Complexity Analysis

### Linear Search
- **Best case**: O(1) - phần tử cần tìm ở đầu mảng
- **Average case**: O(n/2) = O(n)
- **Worst case**: O(n) - phần tử cần tìm ở cuối mảng hoặc không có

### Binary Search
- **Best case**: O(1) - phần tử cần tìm ở giữa mảng
- **Average case**: O(log n)
- **Worst case**: O(log n)

### So sánh
```python
import time
import random

def compare_search_algorithms():
    # Tạo mảng test
    n = 100000
    arr = sorted([random.randint(1, 1000000) for _ in range(n)])
    target = arr[n//2]  # Chọn phần tử ở giữa
    
    # Test Linear Search
    start = time.time()
    linear_search(arr, target)
    linear_time = time.time() - start
    
    # Test Binary Search
    start = time.time()
    binary_search(arr, target)
    binary_time = time.time() - start
    
    print(f"Linear Search: {linear_time:.6f}s")
    print(f"Binary Search: {binary_time:.6f}s")
    print(f"Tỉ lệ: {linear_time/binary_time:.2f}x")

compare_search_algorithms()
```

## When to Use Each Method

### Linear Search
- **Ưu điểm**:
  - Đơn giản, dễ implement
  - Không yêu cầu mảng sắp xếp
  - Hiệu quả với mảng nhỏ
- **Nhược điểm**:
  - Chậm với mảng lớn O(n)

### Binary Search
- **Ưu điểm**:
  - Rất nhanh O(log n)
  - Hiệu quả với mảng lớn
- **Nhược điểm**:
  - Yêu cầu mảng đã sắp xếp
  - Phức tạp hơn để implement

## Ví dụ thực tế

### Bài 1: Tìm phần tử trong mảng
```python
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    
    for _ in range(q):
        target = int(input())
        result = linear_search(arr, target)
        if result != -1:
            print(f"YES {result}")
        else:
            print("NO")

solve()
```

### Bài 2: Tìm trong mảng sắp xếp
```python
def solve():
    n = int(input())
    arr = list(map(int, input().split()))  # Đã sắp xếp
    q = int(input())
    
    for _ in range(q):
        target = int(input())
        result = binary_search(arr, target)
        if result != -1:
            print(f"YES {result}")
        else:
            print("NO")

solve()
```

### Bài 3: Tìm số lần xuất hiện
```python
def count_occurrences(arr, target):
    """Đếm số lần xuất hiện của target trong mảng sắp xếp"""
    def find_first():
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Tìm vị trí đầu tiên
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    def find_last():
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                left = mid + 1  # Tìm vị trí cuối cùng
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    first = find_first()
    if first == -1:
        return 0
    last = find_last()
    return last - first + 1

arr = [1, 2, 2, 2, 3, 4, 4, 5]
target = 2
count = count_occurrences(arr, target)
print(f"Số {target} xuất hiện {count} lần")  # 3 lần
```

## Built-in Functions

### Python built-in search
```python
# Kiểm tra phần tử có tồn tại
arr = [1, 3, 5, 7, 9]
print(5 in arr)  # True
print(4 in arr)  # False

# Tìm index (linear search)
try:
    index = arr.index(5)
    print(f"Tìm thấy tại vị trí {index}")
except ValueError:
    print("Không tìm thấy")

# Binary search với bisect module
import bisect
arr = [1, 3, 5, 7, 9]  # Đã sắp xếp
pos = bisect.bisect_left(arr, 5)
if pos < len(arr) and arr[pos] == 5:
    print(f"Tìm thấy tại vị trí {pos}")
else:
    print("Không tìm thấy")
```