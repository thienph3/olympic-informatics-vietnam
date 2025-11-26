# Day 18: Sắp xếp ứng dụng, Stable Sorting, Custom Comparators

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Hiểu khái niệm stable sorting và tầm quan trọng
- Thành thạo custom comparators và key functions
- Áp dụng sắp xếp vào các bài toán thực tế
- Sắp xếp multi-criteria và nested sorting
- Tối ưu hóa thuật toán sắp xếp cho từng trường hợp cụ thể

## Phần 1: Stable Sorting (45 phút)

### 1.1 Khái niệm Stable Sorting

**Stable sorting** là thuật toán sắp xếp giữ nguyên thứ tự tương đối của các phần tử có giá trị bằng nhau.

**Ví dụ:**
```
Input:  [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
Stable: [(1, 'b'), (2, 'd'), (3, 'a'), (3, 'c')]  # 'a' vẫn trước 'c'
Unstable: [(1, 'b'), (2, 'd'), (3, 'c'), (3, 'a')]  # thứ tự đảo
```

### 1.2 Thuật toán Stable vs Unstable

**Stable algorithms:**
- Merge sort, Insertion sort, Bubble sort
- Counting sort, Radix sort, Bucket sort
- Python's sorted() và list.sort()

**Unstable algorithms:**
- Quick sort, Heap sort, Selection sort

### 1.3 Implementation Stable Sort

```python
def stable_sort_key(arr, key_func):
    """
    Stable sort với key function
    """
    # Python's sort is stable by default
    return sorted(arr, key=key_func)

def make_stable(sort_func):
    """
    Biến thuật toán unstable thành stable
    """
    def stable_wrapper(arr, key=None):
        # Thêm index để đảm bảo stability
        indexed = [(item, i) for i, item in enumerate(arr)]
        
        if key:
            indexed.sort(key=lambda x: (key(x[0]), x[1]))
        else:
            indexed.sort(key=lambda x: (x[0], x[1]))
        
        return [item for item, _ in indexed]
    
    return stable_wrapper
```

## Phần 2: Custom Comparators và Key Functions (45 phút)

### 2.1 Key Functions

```python
# Sắp xếp theo độ dài chuỗi
words = ["apple", "pie", "banana", "cat"]
sorted_words = sorted(words, key=len)

# Sắp xếp theo giá trị tuyệt đối
numbers = [-5, 2, -1, 4, -3]
sorted_abs = sorted(numbers, key=abs)

# Sắp xếp phức tạp
students = [("Alice", 85), ("Bob", 90), ("Charlie", 85)]
# Sắp xếp theo điểm giảm dần, tên tăng dần
sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
```

### 2.2 Multiple Criteria Sorting

```python
def multi_key_sort(arr, keys):
    """
    Sắp xếp theo nhiều tiêu chí
    keys: list of (key_func, reverse) tuples
    """
    result = arr.copy()
    
    # Sắp xếp từ tiêu chí cuối về đầu
    for key_func, reverse in reversed(keys):
        result.sort(key=key_func, reverse=reverse)
    
    return result

# Ví dụ sử dụng
data = [("Alice", 85, 20), ("Bob", 90, 19), ("Charlie", 85, 21)]
# Sắp xếp theo: điểm (giảm), tuổi (tăng), tên (tăng)
keys = [
    (lambda x: x[1], True),   # điểm giảm dần
    (lambda x: x[2], False),  # tuổi tăng dần  
    (lambda x: x[0], False)   # tên tăng dần
]
result = multi_key_sort(data, keys)
```

### 2.3 Custom Comparison Class

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __eq__(self, other):
        return (self.grade, self.age, self.name) == (other.grade, other.age, other.name)
    
    def __lt__(self, other):
        # Sắp xếp theo điểm giảm dần, tuổi tăng dần, tên tăng dần
        return (-self.grade, self.age, self.name) < (-other.grade, other.age, other.name)
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade}, {self.age})"
```

## Phần 3: Ứng dụng Sắp xếp Thực tế (45 phút)

### 3.1 Sắp xếp Intervals

```python
def sort_intervals(intervals):
    """
    Sắp xếp khoảng thời gian theo start time, sau đó end time
    """
    return sorted(intervals, key=lambda x: (x[0], x[1]))

def merge_intervals(intervals):
    """
    Gộp các khoảng thời gian chồng lấp
    """
    if not intervals:
        return []
    
    sorted_intervals = sort_intervals(intervals)
    merged = [sorted_intervals[0]]
    
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Chồng lấp
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged
```

### 3.2 Sắp xếp theo Frequency

```python
def sort_by_frequency(arr):
    """
    Sắp xếp theo tần suất xuất hiện
    """
    from collections import Counter
    
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

def top_k_frequent(arr, k):
    """
    Tìm k phần tử xuất hiện nhiều nhất
    """
    from collections import Counter
    
    freq = Counter(arr)
    return sorted(freq.keys(), key=freq.get, reverse=True)[:k]
```

### 3.3 Sắp xếp Geometric Objects

```python
import math

def sort_points_by_distance(points, origin=(0, 0)):
    """
    Sắp xếp điểm theo khoảng cách từ gốc tọa độ
    """
    def distance(point):
        return math.sqrt((point[0] - origin[0])**2 + (point[1] - origin[1])**2)
    
    return sorted(points, key=distance)

def sort_points_by_angle(points, origin=(0, 0)):
    """
    Sắp xếp điểm theo góc polar
    """
    def angle(point):
        return math.atan2(point[1] - origin[1], point[0] - origin[0])
    
    return sorted(points, key=angle)
```

## Phần 4: Tối ưu hóa và Kỹ thuật Nâng cao (45 phút)

### 4.1 Partial Sorting

```python
import heapq

def partial_sort(arr, k):
    """
    Chỉ sắp xếp k phần tử nhỏ nhất
    Time: O(n log k), Space: O(k)
    """
    return heapq.nsmallest(k, arr)

def kth_element(arr, k):
    """
    Tìm phần tử thứ k mà không sắp xếp toàn bộ
    """
    return heapq.nsmallest(k, arr)[-1]
```

### 4.2 External Sorting Simulation

```python
def external_sort_simulation(data, chunk_size):
    """
    Mô phỏng external sorting cho dữ liệu lớn
    """
    chunks = []
    
    # Chia thành chunks và sắp xếp từng chunk
    for i in range(0, len(data), chunk_size):
        chunk = sorted(data[i:i + chunk_size])
        chunks.append(chunk)
    
    # Merge tất cả chunks
    return merge_sorted_chunks(chunks)

def merge_sorted_chunks(chunks):
    """
    Merge nhiều chunks đã sắp xếp
    """
    import heapq
    
    # Priority queue chứa (value, chunk_index, element_index)
    heap = []
    
    # Khởi tạo heap với phần tử đầu của mỗi chunk
    for i, chunk in enumerate(chunks):
        if chunk:
            heapq.heappush(heap, (chunk[0], i, 0))
    
    result = []
    
    while heap:
        value, chunk_idx, elem_idx = heapq.heappop(heap)
        result.append(value)
        
        # Thêm phần tử tiếp theo từ chunk này
        if elem_idx + 1 < len(chunks[chunk_idx]):
            next_value = chunks[chunk_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, chunk_idx, elem_idx + 1))
    
    return result
```

### 4.3 Adaptive Sorting

```python
def adaptive_sort(arr):
    """
    Thuật toán sắp xếp thích ứng
    """
    n = len(arr)
    
    # Kiểm tra đã sắp xếp
    if is_sorted(arr):
        return arr
    
    # Kiểm tra sắp xếp ngược
    if is_reverse_sorted(arr):
        return arr[::-1]
    
    # Kiểm tra gần như đã sắp xếp
    if nearly_sorted(arr):
        return insertion_sort(arr)
    
    # Sử dụng thuật toán tổng quát
    return sorted(arr)

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def is_reverse_sorted(arr):
    return all(arr[i] >= arr[i+1] for i in range(len(arr)-1))

def nearly_sorted(arr, threshold=0.1):
    """Kiểm tra mảng gần như đã sắp xếp"""
    inversions = count_inversions(arr)
    return inversions <= threshold * len(arr)
```

## Bài tập thực hành

1. **[problem180101.py]** - Stable sorting implementations
2. **[problem180102.py]** - Stable vs unstable comparison
3. **[problem180201.py]** - Custom comparators và key functions
4. **[problem180202.py]** - Multi-criteria sorting
5. **[problem180301.py]** - Interval sorting và merging
6. **[problem180302.py]** - Frequency và geometric sorting
7. **[problem180401.py]** - Partial sorting và optimization
8. **[problem180402.py]** - Advanced sorting applications

## Tổng kết

- Stable sorting quan trọng khi cần giữ thứ tự tương đối
- Custom comparators cho phép sắp xếp theo tiêu chí phức tạp
- Multi-criteria sorting cần sắp xếp từ tiêu chí cuối về đầu
- Partial sorting hiệu quả khi chỉ cần một phần kết quả
- Adaptive sorting tự động chọn thuật toán phù hợp