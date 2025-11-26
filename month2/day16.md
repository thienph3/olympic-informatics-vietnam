# Day 16: Sắp xếp cơ bản (bubble, selection, insertion)

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Bubble Sort (45')

### 📚 Lý thuyết (15')

#### Bubble Sort cơ bản
```python
def bubble_sort(arr):
    """
    Bubble sort - sắp xếp nổi bọt
    Time complexity: O(n²)
    Space complexity: O(1)
    Stable: Yes
    """
    n = len(arr)
    
    for i in range(n):
        # Flag để kiểm tra có swap nào không
        swapped = False
        
        # Last i elements đã được sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Nếu không có swap nào, array đã sorted
        if not swapped:
            break
    
    return arr

# Ví dụ sử dụng
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
bubble_sort(arr)
print(f"Sorted: {arr}")
```

#### Bubble Sort optimizations
```python
def bubble_sort_optimized(arr):
    """
    Optimized bubble sort với early termination
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        # Optimize: giảm range vì phần cuối đã sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Early termination nếu không có swap
        if not swapped:
            break
    
    return arr

def cocktail_shaker_sort(arr):
    """
    Cocktail Shaker Sort - bidirectional bubble sort
    """
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True
    
    while swapped:
        swapped = False
        
        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        end -= 1
        swapped = False
        
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1
    
    return arr
```

#### Bubble Sort với custom comparator
```python
def bubble_sort_custom(arr, key=None, reverse=False):
    """
    Bubble sort với custom key function và reverse order
    """
    n = len(arr)
    
    def compare(a, b):
        if key:
            a, b = key(a), key(b)
        if reverse:
            return a < b
        return a > b
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

# Ví dụ: sort theo độ dài string
words = ["python", "java", "c", "javascript", "go"]
bubble_sort_custom(words, key=len)
print(f"Sorted by length: {words}")

# Sort tuples theo element thứ 2
pairs = [(1, 3), (2, 1), (3, 2)]
bubble_sort_custom(pairs, key=lambda x: x[1])
print(f"Sorted by second element: {pairs}")
```

### 💻 Thực hành (30')

#### Bài tập 1: Bubble sort implementations

**Yêu cầu:** Implement bubble sort và các optimizations.

**File thực hành:** [problem160101.py](problem160101.py)

#### Bài tập 2: Bubble sort applications

**Yêu cầu:** Ứng dụng bubble sort trong các bài toán thực tế.

**File thực hành:** [problem160102.py](problem160102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Selection Sort (45')

### 📚 Lý thuyết (20')

#### Selection Sort cơ bản
```python
def selection_sort(arr):
    """
    Selection sort - chọn phần tử nhỏ nhất
    Time complexity: O(n²)
    Space complexity: O(1)
    Stable: No (có thể làm stable)
    """
    n = len(arr)
    
    for i in range(n):
        # Tìm index của phần tử nhỏ nhất trong phần chưa sort
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap phần tử nhỏ nhất với phần tử đầu tiên chưa sort
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Ví dụ sử dụng
arr = [64, 25, 12, 22, 11]
print(f"Original: {arr}")
selection_sort(arr)
print(f"Sorted: {arr}")
```

#### Selection Sort variants
```python
def selection_sort_stable(arr):
    """
    Stable version của selection sort
    """
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        # Tìm phần tử nhỏ nhất
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Shift elements thay vì swap để maintain stability
        min_val = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = min_val
    
    return arr

def double_selection_sort(arr):
    """
    Double selection sort - tìm min và max cùng lúc
    """
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        min_idx = left
        max_idx = left
        
        # Tìm min và max trong range [left, right]
        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i
        
        # Swap min với left
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        
        # Nếu max_idx bị swap, update nó
        if max_idx == left:
            max_idx = min_idx
        
        # Swap max với right
        arr[right], arr[max_idx] = arr[max_idx], arr[right]
        
        left += 1
        right -= 1
    
    return arr

def selection_sort_recursive(arr, start=0):
    """
    Recursive selection sort
    """
    n = len(arr)
    
    if start >= n - 1:
        return arr
    
    # Tìm min trong phần còn lại
    min_idx = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    # Swap
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    
    # Recursive call
    return selection_sort_recursive(arr, start + 1)
```

#### Selection Sort cho special cases
```python
def selection_sort_k_smallest(arr, k):
    """
    Chỉ sort k phần tử nhỏ nhất
    Time complexity: O(k*n)
    """
    n = len(arr)
    
    for i in range(min(k, n)):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def selection_sort_with_tracking(arr):
    """
    Selection sort với tracking số comparisons và swaps
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return arr, comparisons, swaps
```

### 💻 Thực hành (25')

#### Bài tập 1: Selection sort implementations

**Yêu cầu:** Implement selection sort và variants.

**File thực hành:** [problem160201.py](problem160201.py)

#### Bài tập 2: Selection sort optimizations

**Yêu cầu:** Optimize selection sort cho special cases.

**File thực hành:** [problem160202.py](problem160202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Insertion Sort (45')

### 📚 Lý thuyết (15')

#### Insertion Sort cơ bản
```python
def insertion_sort(arr):
    """
    Insertion sort - chèn phần tử vào vị trí đúng
    Time complexity: O(n²) worst case, O(n) best case
    Space complexity: O(1)
    Stable: Yes
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Di chuyển các phần tử lớn hơn key về phía sau
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Chèn key vào vị trí đúng
        arr[j + 1] = key
    
    return arr

# Ví dụ sử dụng
arr = [12, 11, 13, 5, 6]
print(f"Original: {arr}")
insertion_sort(arr)
print(f"Sorted: {arr}")
```

#### Insertion Sort optimizations
```python
def binary_insertion_sort(arr):
    """
    Binary insertion sort - sử dụng binary search để tìm vị trí chèn
    Time complexity: O(n²) (shifting vẫn là O(n))
    Comparisons: O(n log n)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Binary search để tìm vị trí chèn
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid
            else:
                left = mid + 1
        
        # Shift elements và insert
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
    
    return arr

def insertion_sort_with_sentinel(arr):
    """
    Insertion sort với sentinel để giảm boundary checking
    """
    if not arr:
        return arr
    
    # Tìm min element và đặt ở đầu làm sentinel
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    arr[0], arr[min_idx] = arr[min_idx], arr[0]
    
    # Insertion sort không cần check j >= 0
    for i in range(2, len(arr)):
        key = arr[i]
        j = i - 1
        
        while arr[j] > key:  # Không cần check j >= 0
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def insertion_sort_recursive(arr, n=None):
    """
    Recursive insertion sort
    """
    if n is None:
        n = len(arr)
    
    if n <= 1:
        return arr
    
    # Sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert last element at correct position
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = last
    
    return arr
```

#### Insertion Sort cho linked lists
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertion_sort_list(head):
    """
    Insertion sort cho linked list
    Time complexity: O(n²)
    Space complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    current = head
    
    while current:
        next_node = current.next
        
        # Tìm vị trí để insert current
        prev = dummy
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        
        # Insert current sau prev
        current.next = prev.next
        prev.next = current
        
        current = next_node
    
    return dummy.next

def array_to_list(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def list_to_array(head):
    """Convert linked list to array"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result
```

### 💻 Thực hành (30')

#### Bài tập 1: Insertion sort implementations

**Yêu cầu:** Implement insertion sort và optimizations.

**File thực hành:** [problem160301.py](problem160301.py)

#### Bài tập 2: Insertion sort applications

**Yêu cầu:** Ứng dụng insertion sort cho different data structures.

**File thực hành:** [problem160302.py](problem160302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: So sánh và ứng dụng (45')

### 📚 Lý thuyết (15')

#### So sánh các thuật toán
```python
import time
import random

def compare_sorting_algorithms(arr_size=1000, num_tests=5):
    """
    So sánh hiệu suất các thuật toán sorting
    """
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Binary Insertion': binary_insertion_sort
    }
    
    results = {}
    
    for name, func in algorithms.items():
        total_time = 0
        
        for _ in range(num_tests):
            # Tạo random array
            test_arr = [random.randint(1, 1000) for _ in range(arr_size)]
            
            start = time.time()
            func(test_arr.copy())
            end = time.time()
            
            total_time += end - start
        
        avg_time = total_time / num_tests
        results[name] = avg_time
    
    return results

def analyze_best_worst_cases():
    """
    Phân tích best case và worst case
    """
    n = 1000
    
    # Best case: already sorted
    best_case = list(range(n))
    
    # Worst case: reverse sorted
    worst_case = list(range(n, 0, -1))
    
    # Average case: random
    avg_case = [random.randint(1, n) for _ in range(n)]
    
    cases = {
        'Best (sorted)': best_case,
        'Worst (reverse)': worst_case,
        'Average (random)': avg_case
    }
    
    algorithms = {
        'Bubble': bubble_sort,
        'Selection': selection_sort,
        'Insertion': insertion_sort
    }
    
    results = {}
    
    for case_name, test_arr in cases.items():
        results[case_name] = {}
        
        for alg_name, func in algorithms.items():
            start = time.time()
            func(test_arr.copy())
            end = time.time()
            
            results[case_name][alg_name] = end - start
    
    return results
```

#### Khi nào sử dụng thuật toán nào
```python
def choose_sorting_algorithm(arr_size, data_characteristics):
    """
    Chọn thuật toán sorting phù hợp
    
    Args:
        arr_size: Kích thước array
        data_characteristics: dict với info về data
    """
    
    # Small arrays
    if arr_size <= 10:
        return "Insertion Sort - tốt cho small arrays"
    
    # Nearly sorted data
    if data_characteristics.get('nearly_sorted', False):
        return "Insertion Sort - O(n) cho nearly sorted data"
    
    # Memory constrained
    if data_characteristics.get('memory_limited', False):
        return "Selection Sort - ít swaps nhất"
    
    # Stable sorting required
    if data_characteristics.get('stable_required', False):
        return "Insertion Sort hoặc Bubble Sort - stable algorithms"
    
    # General case
    if arr_size < 50:
        return "Insertion Sort - tốt nhất cho small to medium arrays"
    else:
        return "Nên sử dụng advanced algorithms (merge/quick sort)"

# Ví dụ sử dụng
scenarios = [
    (5, {'nearly_sorted': True}),
    (100, {'memory_limited': True}),
    (50, {'stable_required': True}),
    (1000, {})
]

for size, chars in scenarios:
    recommendation = choose_sorting_algorithm(size, chars)
    print(f"Array size {size}, characteristics {chars}:")
    print(f"  Recommendation: {recommendation}")
```

#### Hybrid sorting approach
```python
def hybrid_sort(arr, threshold=10):
    """
    Hybrid sorting: sử dụng insertion sort cho small subarrays
    """
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        # Placeholder cho advanced algorithms
        return sorted(arr)  # Python's built-in sort

def adaptive_insertion_sort(arr):
    """
    Adaptive insertion sort - detect và handle different patterns
    """
    n = len(arr)
    
    # Check if already sorted
    if all(arr[i] <= arr[i+1] for i in range(n-1)):
        return arr
    
    # Check if reverse sorted
    if all(arr[i] >= arr[i+1] for i in range(n-1)):
        return arr[::-1]
    
    # Use regular insertion sort
    return insertion_sort(arr)
```

### 💻 Thực hành (30')

#### Bài tập 1: Algorithm comparison và analysis

**Yêu cầu:** So sánh performance và analyze characteristics.

**File thực hành:** [problem160401.py](problem160401.py)

#### Bài tập 2: Practical sorting applications

**Yêu cầu:** Ứng dụng sorting trong Olympic problems.

**File thực hành:** [problem160402.py](problem160402.py)

---

## Bài tập về nhà

### Bài 1: Sorting Algorithm Library
Tạo comprehensive sorting library:
- All basic sorting algorithms với optimizations
- Performance benchmarking tools
- Adaptive algorithm selection
- Custom comparator support
- Stability analysis tools

### Bài 2: Olympic Sorting Problems
Giải các bài toán Olympic:
- Sorting với constraints
- Partial sorting problems
- Sorting-based optimization
- Custom sorting criteria
- Multi-key sorting

### Bài 3: Sorting Visualization
Tạo visualization tool:
- Animate sorting process
- Compare algorithms side-by-side
- Show complexity analysis
- Interactive parameter tuning
- Educational demonstrations

### Gợi ý làm bài
1. Understand stability và khi nào cần stable sorting
2. Practice với different data patterns
3. Focus on optimization techniques
4. Master custom comparator usage

---

## Tổng kết Day 16

**Đã học:**
- Bubble Sort: cơ bản, optimizations, cocktail shaker
- Selection Sort: cơ bản, stable version, double selection
- Insertion Sort: cơ bản, binary insertion, linked list
- Comparison: performance analysis, algorithm selection

**Complexity Summary:**
- **Bubble Sort:** O(n²) average/worst, O(n) best, Stable
- **Selection Sort:** O(n²) all cases, Unstable (có thể stable)
- **Insertion Sort:** O(n²) worst, O(n) best, Stable

**Khi nào sử dụng:**
- **Bubble Sort:** Educational purposes, nearly sorted data
- **Selection Sort:** Memory constrained, minimize swaps
- **Insertion Sort:** Small arrays, nearly sorted data, online algorithms

**Chuẩn bị Day 17:**
- Ôn tập basic sorting concepts
- Tìm hiểu non-comparison sorting
- Chuẩn bị cho counting, radix, bucket sort
- Review time complexity analysis