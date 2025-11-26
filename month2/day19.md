# Day 19: Merge Sort, Quick Sort, Heap Sort

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Hiểu và implement merge sort với độ phức tạp O(n log n)
- Thành thạo quick sort và các kỹ thuật tối ưu
- Nắm vững heap sort và cấu trúc heap
- So sánh ưu nhược điểm của từng thuật toán
- Áp dụng vào các bài toán Olympic thực tế

## Phần 1: Merge Sort (45 phút)

### 1.1 Nguyên lý Merge Sort

Merge sort sử dụng chiến lược "chia để trị":
1. **Chia:** Chia mảng thành 2 nửa
2. **Trị:** Đệ quy sắp xếp từng nửa
3. **Kết hợp:** Merge 2 nửa đã sắp xếp

**Ưu điểm:**
- Độ phức tạp ổn định O(n log n)
- Stable sorting
- Predictable performance

**Nhược điểm:**
- Space complexity O(n)
- Không in-place

### 1.2 Implementation Cơ bản

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 1.3 Merge Sort In-place

```python
def merge_sort_inplace(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    # Tạo temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
```

## Phần 2: Quick Sort (45 phút)

### 2.1 Nguyên lý Quick Sort

Quick sort cũng sử dụng "chia để trị":
1. **Chọn pivot:** Chọn một phần tử làm pivot
2. **Partition:** Chia mảng thành 2 phần quanh pivot
3. **Đệ quy:** Sắp xếp từng phần

**Ưu điểm:**
- Average case O(n log n)
- In-place sorting
- Cache-friendly

**Nhược điểm:**
- Worst case O(n²)
- Không stable
- Performance phụ thuộc pivot selection

### 2.2 Implementation Cơ bản

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Chọn phần tử cuối làm pivot
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### 2.3 Quick Sort Optimizations

```python
import random

def quick_sort_optimized(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    while low < high:
        # Sử dụng insertion sort cho mảng nhỏ
        if high - low < 10:
            insertion_sort_range(arr, low, high)
            break
        
        # Random pivot để tránh worst case
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        pivot_index = partition(arr, low, high)
        
        # Đệ quy phần nhỏ hơn, iteration phần lớn hơn
        if pivot_index - low < high - pivot_index:
            quick_sort_optimized(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quick_sort_optimized(arr, pivot_index + 1, high)
            high = pivot_index - 1

def insertion_sort_range(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

## Phần 3: Heap Sort (45 phút)

### 3.1 Nguyên lý Heap Sort

Heap sort sử dụng cấu trúc heap:
1. **Build heap:** Tạo max heap từ mảng
2. **Extract max:** Lấy max (root) và đặt ở cuối
3. **Heapify:** Khôi phục tính chất heap
4. **Lặp lại** cho đến khi hết phần tử

**Ưu điểm:**
- Độ phức tạp ổn định O(n log n)
- In-place sorting
- Space complexity O(1)

**Nhược điểm:**
- Không stable
- Không adaptive
- Cache performance kém

### 3.2 Implementation Heap Sort

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements từ heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify(arr, i, 0)  # Heapify reduced heap

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### 3.3 Heap Operations

```python
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        if not self.heap:
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._heapify_down(0)
        
        return max_val
    
    def _heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def _heapify_down(self, i):
        while self.left_child(i) < len(self.heap):
            max_child = self._max_child_index(i)
            if self.heap[i] < self.heap[max_child]:
                self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
                i = max_child
            else:
                break
    
    def _max_child_index(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        
        if right >= len(self.heap):
            return left
        
        return left if self.heap[left] > self.heap[right] else right
```

## Phần 4: So sánh và Ứng dụng (45 phút)

### 4.1 Bảng So sánh

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | In-place |
|-----------|-----------|--------------|------------|-------|--------|----------|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |

### 4.2 Khi nào sử dụng

**Merge Sort:**
- Cần stable sorting
- Dữ liệu lớn, có thể sử dụng external memory
- Performance predictable quan trọng

**Quick Sort:**
- Cần in-place sorting
- Average case performance tốt
- Memory hạn chế

**Heap Sort:**
- Cần worst-case guarantee O(n log n)
- Memory rất hạn chế
- Không cần stable

### 4.3 Hybrid Algorithms

```python
def intro_sort(arr, max_depth=None):
    """
    Introsort: Quick sort + Heap sort + Insertion sort
    """
    if max_depth is None:
        import math
        max_depth = 2 * int(math.log2(len(arr)))
    
    _intro_sort_helper(arr, 0, len(arr) - 1, max_depth)

def _intro_sort_helper(arr, low, high, max_depth):
    if high - low < 16:
        insertion_sort_range(arr, low, high)
    elif max_depth == 0:
        heap_sort_range(arr, low, high)
    else:
        pivot = partition(arr, low, high)
        _intro_sort_helper(arr, low, pivot - 1, max_depth - 1)
        _intro_sort_helper(arr, pivot + 1, high, max_depth - 1)
```

## Bài tập thực hành

1. **[problem190101.py]** - Merge sort implementations
2. **[problem190102.py]** - Merge sort applications
3. **[problem190201.py]** - Quick sort implementations
4. **[problem190202.py]** - Quick sort optimizations
5. **[problem190301.py]** - Heap sort implementations
6. **[problem190302.py]** - Heap operations và applications
7. **[problem190401.py]** - Algorithm comparison và analysis
8. **[problem190402.py]** - Hybrid sorting algorithms

## Tổng kết

- Merge sort: Stable, predictable O(n log n), cần O(n) memory
- Quick sort: Fast average case, in-place, worst case O(n²)
- Heap sort: Guaranteed O(n log n), in-place, không stable
- Chọn thuật toán dựa trên yêu cầu cụ thể về memory, stability, performance
- Hybrid algorithms kết hợp ưu điểm của nhiều thuật toán