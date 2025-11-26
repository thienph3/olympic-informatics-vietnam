# Day 14: Binary search nâng cao, bisect module, search variants

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Binary Search nâng cao (45')

### 📚 Lý thuyết (15')

#### Lower bound và Upper bound
```python
def lower_bound(arr, target):
    """
    Tìm vị trí đầu tiên >= target (leftmost insertion point)
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index đầu tiên có arr[i] >= target
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def upper_bound(arr, target):
    """
    Tìm vị trí đầu tiên > target (rightmost insertion point)
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index đầu tiên có arr[i] > target
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Ví dụ sử dụng
arr = [1, 2, 2, 2, 3, 4, 4, 5]
target = 2
print(f"Lower bound của {target}: {lower_bound(arr, target)}")  # 1
print(f"Upper bound của {target}: {upper_bound(arr, target)}")  # 4
```

#### Binary search với custom comparator
```python
def binary_search_custom(arr, target, key_func=None, reverse=False):
    """
    Binary search với custom key function và reverse order
    Input: arr - sorted array, target, key_func - transform function, reverse - sort order
    Output: index của target hoặc -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = key_func(arr[mid]) if key_func else arr[mid]
        target_val = key_func(target) if key_func else target
        
        if mid_val == target_val:
            return mid
        
        if not reverse:
            if mid_val < target_val:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if mid_val > target_val:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Ví dụ: tìm kiếm trong array of tuples
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("David", 92)]
students.sort(key=lambda x: x[1])  # Sort by grade

target_student = ("Unknown", 90)
result = binary_search_custom(students, target_student, key_func=lambda x: x[1])
print(f"Student với điểm 90: {students[result] if result != -1 else 'Not found'}")
```

#### Binary search trên floating point
```python
def binary_search_float(func, target, left, right, epsilon=1e-9):
    """
    Binary search trên floating point với function
    Input: func - monotonic function, target - target value, left/right - bounds, epsilon - precision
    Output: x sao cho func(x) ≈ target
    """
    while right - left > epsilon:
        mid = (left + right) / 2
        mid_val = func(mid)
        
        if abs(mid_val - target) < epsilon:
            return mid
        elif mid_val < target:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2

# Ví dụ: tìm căn bậc hai
def square(x):
    return x * x

sqrt_5 = binary_search_float(square, 5, 0, 5)
print(f"Căn bậc hai của 5: {sqrt_5:.6f}")
```

#### Binary search với overflow protection
```python
def binary_search_safe(arr, target):
    """
    Binary search với protection khỏi integer overflow
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Tránh overflow: mid = left + (right - left) // 2
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Template cho binary search variants
def binary_search_template(arr, condition_func):
    """
    Template tổng quát cho binary search variants
    Input: arr - sorted array, condition_func - function trả về True/False
    Output: index thỏa mãn điều kiện
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if condition_func(arr[mid]):
            result = mid
            # Tùy thuộc vào bài toán, có thể tìm left hoặc right
            right = mid - 1  # Tìm leftmost
            # left = mid + 1  # Tìm rightmost
        else:
            left = mid + 1
    
    return result
```

### 💻 Thực hành (30')

#### Bài tập 1: Lower/Upper bound implementations

**Yêu cầu:** Implement lower_bound, upper_bound và applications.

**File thực hành:** [problem140101.py](problem140101.py)

#### Bài tập 2: Custom binary search variants

**Yêu cầu:** Binary search với custom comparators và floating point.

**File thực hành:** [problem140102.py](problem140102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Bisect module trong Python (45')

### 📚 Lý thuyết (20')

#### Giới thiệu bisect module
```python
import bisect

# Bisect module cung cấp binary search functions
arr = [1, 3, 4, 4, 6, 8, 9]

# bisect_left: tương đương lower_bound
pos = bisect.bisect_left(arr, 4)
print(f"bisect_left(4): {pos}")  # 2

# bisect_right: tương đương upper_bound  
pos = bisect.bisect_right(arr, 4)
print(f"bisect_right(4): {pos}")  # 4

# bisect: alias cho bisect_right
pos = bisect.bisect(arr, 4)
print(f"bisect(4): {pos}")  # 4
```

#### Insertion operations
```python
import bisect

# insort_left: insert và maintain sorted order
arr = [1, 3, 6, 8, 9]
bisect.insort_left(arr, 4)
print(f"After insort_left(4): {arr}")  # [1, 3, 4, 6, 8, 9]

# insort_right: insert at rightmost position
arr = [1, 3, 4, 4, 6, 8, 9]
bisect.insort_right(arr, 4)
print(f"After insort_right(4): {arr}")  # [1, 3, 4, 4, 4, 6, 8, 9]

# insort: alias cho insort_right
arr = [1, 3, 6, 8, 9]
bisect.insort(arr, 5)
print(f"After insort(5): {arr}")  # [1, 3, 5, 6, 8, 9]
```

#### Bisect với key function (Python 3.10+)
```python
import bisect

# Sử dụng key function
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("David", 92)]

# Tìm vị trí để insert student với grade 88
pos = bisect.bisect_left(students, 88, key=lambda x: x[1])
print(f"Insert position for grade 88: {pos}")

# Insert student mới
new_student = ("Eve", 88)
bisect.insort(students, new_student, key=lambda x: x[1])
print(f"After inserting Eve: {students}")
```

#### Practical applications của bisect
```python
import bisect

class SortedList:
    """
    Sorted list implementation using bisect
    Maintains sorted order automatically
    """
    def __init__(self):
        self.data = []
    
    def add(self, item):
        """Add item while maintaining sorted order"""
        bisect.insort(self.data, item)
    
    def remove(self, item):
        """Remove item if exists"""
        pos = bisect.bisect_left(self.data, item)
        if pos < len(self.data) and self.data[pos] == item:
            self.data.pop(pos)
            return True
        return False
    
    def find(self, item):
        """Check if item exists"""
        pos = bisect.bisect_left(self.data, item)
        return pos < len(self.data) and self.data[pos] == item
    
    def count(self, item):
        """Count occurrences of item"""
        left = bisect.bisect_left(self.data, item)
        right = bisect.bisect_right(self.data, item)
        return right - left
    
    def range_query(self, low, high):
        """Get all items in range [low, high]"""
        left = bisect.bisect_left(self.data, low)
        right = bisect.bisect_right(self.data, high)
        return self.data[left:right]

# Ví dụ sử dụng
sorted_list = SortedList()
for item in [3, 1, 4, 1, 5, 9, 2, 6]:
    sorted_list.add(item)

print(f"Sorted list: {sorted_list.data}")
print(f"Count of 1: {sorted_list.count(1)}")
print(f"Range [2, 5]: {sorted_list.range_query(2, 5)}")
```

#### Grade calculation với bisect
```python
import bisect

def calculate_grade(score, breakpoints, grades):
    """
    Calculate letter grade based on score
    Input: score - numeric score, breakpoints - sorted thresholds, grades - corresponding grades
    Output: letter grade
    """
    index = bisect.bisect(breakpoints, score)
    return grades[index]

# Ví dụ: grading system
breakpoints = [60, 70, 80, 90]
grades = ['F', 'D', 'C', 'B', 'A']

scores = [45, 65, 75, 85, 95]
for score in scores:
    grade = calculate_grade(score, breakpoints, grades)
    print(f"Score {score}: Grade {grade}")
```

### 💻 Thực hành (25')

#### Bài tập 1: Bisect module applications

**Yêu cầu:** Sử dụng bisect module cho various applications.

**File thực hành:** [problem140201.py](problem140201.py)

#### Bài tập 2: SortedList implementation

**Yêu cầu:** Build advanced SortedList với bisect module.

**File thực hành:** [problem140202.py](problem140202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Search variants và optimizations (45')

### 📚 Lý thuyết (15')

#### Interpolation Search
```python
def interpolation_search(arr, target):
    """
    Interpolation search - tốt hơn binary search cho uniformly distributed data
    Time complexity: O(log log n) average, O(n) worst case
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # Tránh division by zero
        if arr[right] == arr[left]:
            if arr[left] == target:
                return left
            break
        
        # Interpolation formula
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        # Ensure pos is within bounds
        pos = max(left, min(pos, right))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

# Ví dụ với uniformly distributed data
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70
result = interpolation_search(arr, target)
print(f"Interpolation search tìm {target}: {result}")
```

#### Exponential Search
```python
def exponential_search(arr, target):
    """
    Exponential search - tốt cho unbounded/infinite arrays
    Time complexity: O(log n)
    """
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find range for binary search
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    
    # Binary search trong range [bound//2, min(bound, len(arr)-1)]
    left = bound // 2
    right = min(bound, len(arr) - 1)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Ví dụ
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
target = 15
result = exponential_search(arr, target)
print(f"Exponential search tìm {target}: {result}")
```

#### Fibonacci Search
```python
def fibonacci_search(arr, target):
    """
    Fibonacci search - không cần division, tốt cho systems không có division
    Time complexity: O(log n)
    """
    n = len(arr)
    
    # Generate Fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number
    
    # Find smallest Fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1
    
    while fib_m > 1:
        # Check if fib_m2 is valid location
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    # Check last element
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1
```

#### Ternary Search cho unimodal functions
```python
def ternary_search_max(func, left, right, epsilon=1e-9):
    """
    Ternary search để tìm maximum của unimodal function
    Input: func - unimodal function, left/right - search range, epsilon - precision
    Output: x tại đó func(x) maximum
    """
    while right - left > epsilon:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        
        if func(m1) < func(m2):
            left = m1
        else:
            right = m2
    
    return (left + right) / 2

# Ví dụ: tìm maximum của parabola
def parabola(x):
    return -(x - 3) ** 2 + 10

max_x = ternary_search_max(parabola, 0, 6)
print(f"Maximum của parabola tại x = {max_x:.6f}")
```

### 💻 Thực hành (30')

#### Bài tập 1: Search variants implementation

**Yêu cầu:** Implement interpolation, exponential, fibonacci search.

**File thực hành:** [problem140301.py](problem140301.py)

#### Bài tập 2: Ternary search applications

**Yêu cầu:** Ternary search cho optimization problems.

**File thực hành:** [problem140302.py](problem140302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Advanced applications và Olympic problems (45')

### 📚 Lý thuyết (15')

#### Matrix search algorithms
```python
def search_sorted_matrix(matrix, target):
    """
    Tìm kiếm trong ma trận sorted theo hàng và cột
    Time complexity: O(m + n)
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from top-right
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down
    
    return False

def search_row_col_sorted_matrix(matrix, target):
    """
    Tìm kiếm trong ma trận mỗi hàng và cột đều sorted
    Time complexity: O(m log n)
    """
    for row in matrix:
        pos = bisect.bisect_left(row, target)
        if pos < len(row) and row[pos] == target:
            return True
    return False
```

#### Range query optimizations
```python
class RangeQueryOptimized:
    """
    Optimized range queries using binary search
    """
    def __init__(self, arr):
        self.arr = sorted(arr)
    
    def count_in_range(self, low, high):
        """Count elements in range [low, high]"""
        left = bisect.bisect_left(self.arr, low)
        right = bisect.bisect_right(self.arr, high)
        return right - left
    
    def count_less_than(self, value):
        """Count elements < value"""
        return bisect.bisect_left(self.arr, value)
    
    def count_greater_than(self, value):
        """Count elements > value"""
        return len(self.arr) - bisect.bisect_right(self.arr, value)
    
    def kth_smallest(self, k):
        """Get k-th smallest element (1-indexed)"""
        if 1 <= k <= len(self.arr):
            return self.arr[k - 1]
        return None

# Ví dụ sử dụng
rq = RangeQueryOptimized([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(f"Count in range [2, 5]: {rq.count_in_range(2, 5)}")
print(f"3rd smallest: {rq.kth_smallest(3)}")
```

#### Binary search trên answer space nâng cao
```python
def minimize_maximum_distance(stations, k):
    """
    Minimize maximum distance between consecutive gas stations
    by adding k new stations optimally
    """
    def can_achieve_max_distance(max_dist):
        """Check if we can achieve max_dist with k stations"""
        needed = 0
        for i in range(len(stations) - 1):
            distance = stations[i + 1] - stations[i]
            needed += int(distance / max_dist)
        return needed <= k
    
    left, right = 0, stations[-1] - stations[0]
    epsilon = 1e-6
    
    while right - left > epsilon:
        mid = (left + right) / 2
        if can_achieve_max_distance(mid):
            right = mid
        else:
            left = mid
    
    return left

def split_array_largest_sum(nums, m):
    """
    Split array into m subarrays to minimize largest sum
    """
    def can_split(max_sum):
        """Check if we can split into m parts with max_sum"""
        current_sum = 0
        splits = 1
        
        for num in nums:
            if current_sum + num > max_sum:
                splits += 1
                current_sum = num
                if splits > m:
                    return False
            else:
                current_sum += num
        
        return True
    
    left, right = max(nums), sum(nums)
    
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

### 💻 Thực hành (30')

#### Bài tập 1: Matrix search algorithms

**Yêu cầu:** Implement various matrix search techniques.

**File thực hành:** [problem140401.py](problem140401.py)

#### Bài tập 2: Advanced Olympic problems

**Yêu cầu:** Solve complex Olympic problems using advanced search.

**File thực hành:** [problem140402.py](problem140402.py)

---

## Bài tập về nhà

### Bài 1: Advanced Search Library
Tạo thư viện search algorithms nâng cao:
- All search variants (interpolation, exponential, fibonacci)
- Bisect module wrappers và extensions
- Custom comparators và key functions
- Performance benchmarking tools
- Comprehensive test suite

### Bài 2: Olympic Search Contest
Giải các bài toán Olympic nâng cao:
- Matrix search problems
- Range query optimization
- Binary search on answer space
- Multi-dimensional search problems
- Optimization với constraints

### Bài 3: Search Visualization Tool
Tạo tool visualization cho search algorithms:
- Animate different search algorithms
- Compare performance visually
- Interactive parameter tuning
- Step-by-step execution display
- Complexity analysis charts

### Gợi ý làm bài
1. Master lower_bound/upper_bound concepts
2. Practice với bisect module extensively
3. Understand when to use each search variant
4. Focus on binary search on answer space technique

---

## Tổng kết Day 14

**Đã học:**
- Binary Search nâng cao: lower/upper bound, custom comparators, floating point
- Bisect module: comprehensive usage, key functions, practical applications
- Search variants: interpolation, exponential, fibonacci, ternary search
- Advanced applications: matrix search, range queries, optimization problems

**Kỹ năng đạt được:**
- Master advanced binary search techniques
- Efficiently use Python's bisect module
- Choose appropriate search algorithm for problems
- Solve complex Olympic-level search problems
- Optimize search performance for specific use cases

**Chuẩn bị Day 15:**
- Ôn tập ternary search cho optimization
- Tìm hiểu exponential search applications
- Thực hành interpolation search
- Chuẩn bị cho advanced search techniques