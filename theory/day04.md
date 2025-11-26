# Day 4: Sorting Algorithms

## Merge Sort (Sắp xếp trộn)

### Khái niệm
Merge Sort là thuật toán "chia để trị" (divide and conquer). Chia mảng thành 2 nửa, sắp xếp từng nửa, rồi trộn lại.

### Implementation
```python
def merge_sort(arr):
    """
    Merge Sort implementation
    Time complexity: O(n log n) - tất cả trường hợp
    Space complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Chia mảng thành 2 nửa
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Trộn 2 mảng đã sắp xếp
    return merge(left, right)

def merge(left, right):
    """Trộn 2 mảng đã sắp xếp"""
    result = []
    i = j = 0
    
    # So sánh và trộn
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Thêm phần tử còn lại
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Ví dụ sử dụng
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(f"Mảng gốc: {arr}")
print(f"Đã sắp xếp: {sorted_arr}")
```

### In-place Merge Sort
```python
def merge_sort_inplace(arr, left=0, right=None):
    """Merge sort in-place để tiết kiệm bộ nhớ"""
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    """Trộn in-place"""
    # Tạo mảng tạm
    temp = arr[left:right+1]
    
    i = 0  # Index cho left part
    j = mid - left + 1  # Index cho right part
    k = left  # Index cho mảng gốc
    
    while i <= mid - left and j <= right - left:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1
    
    # Copy phần tử còn lại
    while i <= mid - left:
        arr[k] = temp[i]
        i += 1
        k += 1
    
    while j <= right - left:
        arr[k] = temp[j]
        j += 1
        k += 1
```

## Quick Sort (Sắp xếp nhanh)

### Khái niệm
Quick Sort chọn một phần tử làm pivot, phân hoạch mảng thành 2 phần: nhỏ hơn và lớn hơn pivot, rồi đệ quy sắp xếp.

### Implementation
```python
def quick_sort(arr):
    """
    Quick Sort implementation
    Time complexity: 
    - Average: O(n log n)
    - Worst: O(n²) - khi pivot luôn là min/max
    Space complexity: O(log n) - stack recursion
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Ví dụ sử dụng
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print(f"Đã sắp xếp: {sorted_arr}")
```

### In-place Quick Sort
```python
def quick_sort_inplace(arr, low=0, high=None):
    """Quick sort in-place"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Phân hoạch và lấy pivot index
        pi = partition(arr, low, high)
        
        # Đệ quy sắp xếp 2 phần
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    """Phân hoạch mảng quanh pivot"""
    pivot = arr[high]  # Chọn phần tử cuối làm pivot
    i = low - 1  # Index của phần tử nhỏ hơn
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Ví dụ sử dụng
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_inplace(arr)
print(f"Đã sắp xếp: {arr}")
```

### Randomized Quick Sort
```python
import random

def randomized_quick_sort(arr, low=0, high=None):
    """Quick sort với pivot ngẫu nhiên để tránh worst case"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Chọn pivot ngẫu nhiên
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        
        pi = partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)
```

## Time Complexity Analysis

### Merge Sort
- **Best case**: O(n log n)
- **Average case**: O(n log n)
- **Worst case**: O(n log n)
- **Space**: O(n)

### Quick Sort
- **Best case**: O(n log n)
- **Average case**: O(n log n)
- **Worst case**: O(n²)
- **Space**: O(log n)

### Comparison
```python
import time
import random

def compare_sorting_algorithms():
    # Tạo mảng test
    n = 10000
    arr1 = [random.randint(1, 1000) for _ in range(n)]
    arr2 = arr1.copy()
    arr3 = arr1.copy()
    
    # Test Merge Sort
    start = time.time()
    merge_sort(arr1)
    merge_time = time.time() - start
    
    # Test Quick Sort
    start = time.time()
    quick_sort(arr2)
    quick_time = time.time() - start
    
    # Test Built-in Sort
    start = time.time()
    arr3.sort()
    builtin_time = time.time() - start
    
    print(f"Merge Sort: {merge_time:.6f}s")
    print(f"Quick Sort: {quick_time:.6f}s")
    print(f"Built-in Sort: {builtin_time:.6f}s")

compare_sorting_algorithms()
```

## Built-in Sort vs Custom Sorting

### Python's Built-in Sort
```python
# sort() - sắp xếp in-place
arr = [64, 34, 25, 12, 22, 11, 90]
arr.sort()
print(arr)  # [11, 12, 22, 25, 34, 64, 90]

# sorted() - trả về mảng mới
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = sorted(arr)
print(f"Gốc: {arr}")
print(f"Sắp xếp: {sorted_arr}")

# Sắp xếp giảm dần
arr.sort(reverse=True)
print(arr)  # [90, 64, 34, 25, 22, 12, 11]
```

### Custom Key Function
```python
# Sắp xếp theo độ dài chuỗi
words = ["python", "java", "c", "javascript", "go"]
words.sort(key=len)
print(words)  # ['c', 'go', 'java', 'python', 'javascript']

# Sắp xếp tuple theo phần tử thứ 2
students = [("An", 85), ("Binh", 92), ("Chi", 78)]
students.sort(key=lambda x: x[1])
print(students)  # [('Chi', 78), ('An', 85), ('Binh', 92)]

# Sắp xếp phức tạp
def custom_key(student):
    name, score = student
    return (-score, name)  # Điểm cao trước, tên theo alphabet

students.sort(key=custom_key)
print(students)
```

### Stable vs Unstable Sorting
```python
# Python's sort là stable - giữ thứ tự tương đối
data = [("An", 85), ("Binh", 85), ("Chi", 90)]
data.sort(key=lambda x: x[1])  # Sắp xếp theo điểm
print(data)  # An vẫn trước Binh vì cùng điểm
```

## Ví dụ thực tế

### Bài 1: Sắp xếp cơ bản
```python
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Sử dụng built-in sort
    arr.sort()
    print(*arr)

solve()
```

### Bài 2: Sắp xếp theo tiêu chí
```python
def solve():
    n = int(input())
    students = []
    
    for _ in range(n):
        name, score = input().split()
        students.append((name, int(score)))
    
    # Sắp xếp theo điểm giảm dần, tên tăng dần
    students.sort(key=lambda x: (-x[1], x[0]))
    
    for name, score in students:
        print(f"{name} {score}")

solve()
```

### Bài 3: Merge k sorted arrays
```python
def merge_k_sorted_arrays(arrays):
    """Trộn k mảng đã sắp xếp"""
    import heapq
    
    result = []
    heap = []
    
    # Thêm phần tử đầu của mỗi mảng vào heap
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    while heap:
        val, array_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        # Thêm phần tử tiếp theo từ cùng mảng
        if element_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, array_idx, element_idx + 1))
    
    return result

# Ví dụ
arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
result = merge_k_sorted_arrays(arrays)
print(result)  # [1, 1, 2, 3, 4, 4, 5, 6]
```

### Bài 4: Counting inversions
```python
def count_inversions(arr):
    """Đếm số cặp nghịch thế sử dụng merge sort"""
    def merge_and_count(arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)  # Tất cả phần tử từ i đến mid > arr[j]
                j += 1
            k += 1
        
        # Copy phần tử còn lại
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy back
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_and_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_and_count(arr, temp, left, mid)
            inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
            inv_count += merge_and_count(arr, temp, left, mid, right)
        return inv_count
    
    temp = [0] * len(arr)
    return merge_sort_and_count(arr.copy(), temp, 0, len(arr) - 1)

arr = [8, 4, 2, 1]
inversions = count_inversions(arr)
print(f"Số cặp nghịch thế: {inversions}")  # 6
```

## When to Use Each Algorithm

### Merge Sort
- **Ưu điểm**: Stable, O(n log n) guaranteed, tốt cho linked list
- **Nhược điểm**: Cần O(n) extra space
- **Khi nào dùng**: Cần stable sort, worst-case performance quan trọng

### Quick Sort
- **Ưu điểm**: In-place, average O(n log n), cache-friendly
- **Nhược điểm**: Worst case O(n²), không stable
- **Khi nào dùng**: Bộ nhớ hạn chế, average case performance tốt

### Built-in Sort (Timsort)
- **Ưu điểm**: Highly optimized, stable, adaptive
- **Khi nào dùng**: Hầu hết trường hợp thực tế